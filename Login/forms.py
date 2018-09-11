from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    """docstring for LoginForm. has fields for login page"""
    class Meta:
        model = User
        fields = ['username', 'password']

        labels = {
            "username": 'user'
        }

        widgets = {
            # telling Django your password field in the mode is a password input on the template
            'password': forms.PasswordInput()
        }
