from django import forms
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


class ProfileUpdateForm(forms.Form):
    model = Profile
    field = ['bio', 'avatar', 'country', 'gpa', 'gre_score',
             'toefl_score', 'sop_score', 'lor_score', 'uni_score', 'research']
