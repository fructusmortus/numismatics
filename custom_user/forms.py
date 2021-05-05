from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class':'form-control', 'type':'username'}),
    )
    email = forms.EmailField(
        max_length=100, 
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
    )

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "address", "phone", "email", "password1", "password2"]

        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'address': forms.TextInput(attrs={'class': 'form-control'}),
                'phone': forms.TextInput(attrs={'class': 'form-control'}),
            }
