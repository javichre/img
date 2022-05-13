import email
from enum import unique
from multiprocessing import reduction
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
    widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'usuario'
    }))
    email = forms.EmailField(required=True,
     widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'email'
    }))
    password  = forms.CharField(required=True, min_length=8,
     widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'contraseña'
    }))

    password2 = forms.CharField(label= 'confrimar password', required=True,
    widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'repita contraseña'

    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya esta en uso')
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya esta en uso')
        
        return email

    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2','las contraseñas no coinciden')