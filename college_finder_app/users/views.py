from django.db.utils import ConnectionDoesNotExist, Error
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages
from validate_email import validate_email
from usernames import is_safe_username
import re
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import get_template
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import UserUpdateForm, ProfileUpdateForm
import pickle

username_pattern = re.compile(
    r'^(?=.{5,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$')


class RegistrationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'users/login.html', context={'mode': 'signup', })

    def post(self, request):
        has_error = False
        reg_form = request.POST

        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        reg_username = request.POST.get('reg_username')
        reg_password = request.POST.get('reg_password')
        reg_password_repeat = request.POST.get('reg_password_repeat')

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Please provide a valid email.')
            has_error = True

        try:
            if User.objects.get(email=email):
                messages.add_message(request, messages.ERROR,
                                     'Email is already taken.')
                has_error = True
        except Exception as e:
            pass

        try:
            if User.objects.get(reg_username=reg_username):
                messages.add_message(request, messages.ERROR,
                                     'Username is already taken.')
                has_error = True
        except Exception as e:
            pass

        if not username_pattern.match(reg_username):
            messages.add_message(
                request, messages.ERROR, 'Username can only contain letters (a-z), numbers (0-9), underscores (_), and periods (.) and it must be between 5 and 20 characters.')
            has_error = True

        if not is_safe_username(reg_username):
            messages.add_message(
                request, messages.WARNING, 'Username contains invalid word.')
            has_error = True

        if len(reg_password) < 8:
            messages.add_message(
                request, messages.ERROR, 'Your password must not be less than 8 characters.')
            has_error = True

        if reg_password != reg_password_repeat:
            messages.add_message(request, messages.ERROR,
                                 'Password does not match.')
            has_error = True

        if not has_error:
            try:
                user = User.objects.create(email=email, username=reg_username)
                user.set_password(reg_password)
                user.first_name = fullname.split()[0]
                user.last_name = " ".join(fullname.split()[1:])
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                email_subject = 'Activate your College Finder account'
                message = get_template('users/activate.html').render(context={
                    'user': user,
                    'domain': current_site.domain,
                    'user_id': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': generate_token.make_token(user)
                })

                email_message = EmailMessage(
                    email_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                )
                email_message.content_subtype = 'html'

                email_message.send()

                messages.add_message(request, messages.SUCCESS,
                                     'Account created successfully. Check your email to confirm your account.')
                return redirect('login')

            except (ConnectionError, ConnectionAbortedError, ConnectionRefusedError, ConnectionDoesNotExist, ConnectionResetError):
                messages.add_message(request, messages.ERROR,
                                     'There was connection problems when signing up your account. Please try again with stable connection.')
                has_error = True
                return redirect('register')

            except IntegrityError as e:
                messages.add_message(request, messages.ERROR,
                                     'Username is already taken.')
                has_error = True
                return redirect('register')

        else:
            has_error = True
            return render(request, 'users/login.html', status=400, context={'mode': 'signup', 'reg_form': reg_form, 'error': has_error})


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'users/login.html', context={'mode': 'signin', })

    def post(self, request):
        context = {
            'form': request.POST,
            'has_error': False
        }
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == '':
            messages.add_message(request, messages.ERROR,
                                 'Username is required.')
            context['has_error'] = True

        if password == '':
            messages.add_message(request, messages.ERROR,
                                 'Password is required.')
            context['has_error'] = True

        user = authenticate(request, username=username, password=password)

        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR,
                                 'Invalid Log In credentials.')
            context['has_error'] = True

        if context['has_error']:
            return render(request, 'users/login.html', status=401, context=context)

        login(request, user)
        messages.add_message(request, messages.SUCCESS,
                             'Logged in successfully.')
        return redirect('dashboard')


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=user_id)
        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Account activated successfully. You can sign in to the app with your credentials now.')
            return render(request, 'users/login.html', context={'mode': 'signin'})
        return render(request, 'users/login.html', context={'mode': 'signup'}, status=401)


def logout_page(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Logged out successfully.')
    return redirect('login')


def profile_update_form(request):

    if request.method == 'POST':

        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile has been updated!')
            return redirect('update_profile')

        messages.error(request, f'Something went wrong.')

        return redirect('update_profile')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)

    # Saving Chance of Admit Start
    profile_obj = request.user.profile
    null_count = 0
    for f in ["avatar", "bio", "gpa", "gre_score", "toefl_score", "lor_score", "research"]:
        if getattr(profile_obj, f, None) is None:
            null_count += 1
    profile_completed = int((10 - null_count) / 10 * 100)

    with open('lr_model', 'rb') as f:
        mp = pickle.load(f)

    if profile_completed == 100:
        chance_of_admit = float(mp.predict([[profile_obj.gre_score, profile_obj.toefl_score, profile_obj.uni_score,
                                              profile_obj.sop_score, profile_obj.lor_score,  profile_obj.gpa, profile_obj.research]]))
    else:
        chance_of_admit = 0

    chance_of_admit = chance_of_admit

    profile_obj.chance_of_admit = chance_of_admit
    profile_obj.save()

    # Saving Chance of Admit End

    return render(request, 'users/update-profile.html', {'u_form': u_form, 'p_form': p_form, 'title': 'Update Profile'})
