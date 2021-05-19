from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegisterForm(forms.Form):
    fullname = forms.CharField(max_length=32)
    email = forms.EmailField()
    reg_username = forms.CharField(max_length=20)
    reg_password = forms.CharField(widget=forms.PasswordInput)
    reg_password_repeat = forms.CharField(widget=forms.PasswordInput)


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile

        # SUBJECT TO CHANGE AFTER S3 BUCKET SETUP
        fields = ['bio', 'avatar', 'gpa', 'gre_score',
                  'toefl_score', 'sop_score', 'lor_score', 'uni_score', 'research']
        widgets = {'research': forms.RadioSelect}
