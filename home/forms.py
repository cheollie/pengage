# customize user creation form

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    grade = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'grade']
