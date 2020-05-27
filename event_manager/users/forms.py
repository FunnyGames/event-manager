from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ResetPasswordForm(forms.Form):
    email = forms.EmailField()


class ResetPasswordEnterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['password1', 'password2']
