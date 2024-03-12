from django.contrib.auth.forms import UserCreationForm
from ORVBA.models import *
from django.contrib.auth.models import AbstractBaseUser

from django import forms
from django.contrib.auth.forms import AuthenticationForm


# class UserForm(UserCreationForm):
#     class Meta:
#         model=AbstractBaseUser
#         fields=["username","email","password"]


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
