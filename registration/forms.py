from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_staff = forms.BooleanField(initial=True)

    class Meta:
        model = User
        fields = ['username', 'email','is_staff', 'password1', 'password2']
        widgets = {'is_staff': forms.HiddenInput()}

