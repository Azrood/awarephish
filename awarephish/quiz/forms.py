from django import forms
from .models import Utilisateur,User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

class SignupForm(forms.Form):
    username = forms.CharField(max_length=150, label='Nom d\'utilisateur')
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmer le mot de passe', widget=forms.PasswordInput)
    email = forms.EmailField(label='Adresse Email')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = Utilisateur.user.get_queryset().filter(username=username)
        if r.count():
            raise ValidationError("Nom d'utilisateur déjà pris")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = Utilisateur.user.get_queryset().filter(email=email)
        if r.count():
            raise ValidationError("Cette adresse existe déjà")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Les mtos de passes ne correspondent pas")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class SigninForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': ("Nom d`'utilisateur ou mot de passe incorrect"),
    }