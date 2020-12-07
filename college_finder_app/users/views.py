from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages
from validate_email import validate_email
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import UserRegisterForm, UserLoginForm


class RegistrationView(View):
    def get(self, request):
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

        if len(reg_username) < 5 or len(reg_username) > 14:
            messages.add_message(
                request, messages.ERROR, 'Username must be between 5 and 14 characters.')
            has_error = True

        if len(reg_password) < 8 or len(reg_password) > 20:
            messages.add_message(
                request, messages.ERROR, 'Your password must be between 8 and 20 characters.')
            has_error = True

        if reg_password != reg_password_repeat:
            messages.add_message(request, messages.ERROR,
                                 'Password does not match.')
            has_error = True

        if not has_error:
            try:
                user = User.objects.create(email=email, username=reg_username)
                user.set_password(reg_password)
                user.firstname = fullname
                user.lastname = fullname
                user.is_active = False

                user.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Account created successfully.')
                return redirect('login')
            except IntegrityError as e:
                messages.add_message(request, messages.ERROR,
                                     'Account already exists.')
                has_error = True
                return redirect('login')
        else:
            has_error = True
            return render(request, 'users/login.html', status=400, context={'mode': 'signup', 'reg_form': reg_form, 'error': has_error})

        # print(reg_form)
        # if reg_form.is_valid():
        #     return redirect('register')
        # else:


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html', context={'mode': 'signin', })

    # def get(self, request):
    #     login_form = UserLoginForm(request.POST)
    #     return render(request, 'users/login.html', context={'mode': 'signin', 'login_form': login_form})
