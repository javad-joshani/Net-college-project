from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="ایمبل", required=False)
    phone = forms.CharField(label="تلفن همراه",max_length=14)

    class Meta:
        model = User
        fields = ["username","email","phone","password1","password2"]