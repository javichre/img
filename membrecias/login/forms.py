from pickletools import read_uint1
from pyexpat import model
from django import forms
from django.contrib import admin
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from suscripciones.models import Paciente
from .models import Suscripccion,User

class LogForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'ingrese su contraseña',
            'id':'password1',
            'required':'required',
            }
        ))

    password2 = forms.CharField(label='confirme contraseña',widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'confirme su contraseña',
            'id':'password2',
            'required':'required',
            }
        ))

    class Meta:
        model = User
        fields = ['username','nombres','apellidos','sexo','documento','nacionalidad','ciudad','fecha_nacimiento','telefono','imagen']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya esta en uso')
            
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2
         
    def  save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


############################################################################################################################
class MiembroForm(forms.ModelForm):
    class Meta:
        model = Suscripccion
        fields = ['correo', 'nombres', 'apellidos','sexo', 'documento', 'nacionalidad','ciudad','fecha_nacimiento', 'imagen']

        widgets = {
            
            'correo' : forms.EmailInput(
                attrs = {
                    'class':'form-control col-12',
                    'placeholder' : 'ingresu su correo'
                }
            ),

            'nombres' : forms.TextInput(
                attrs = {
                    'class':'form-control col-12',
                    'placeholder' : 'ingresu su nombre'
                }
            ),

            'apellidos' : forms.TextInput(
                attrs = {
                    'class':'form-control col-12',
                    'placeholder' : 'ingresu su apellido'
                }
            ),

            'documento' : forms.NumberInput(
                attrs = {
                    'class':'form-control col-12',
                    'placeholder' : 'ingresu su documento'
                }
            ),


            'fecha_nacimiento' : forms.DateInput(
                attrs = {
                    'class':'form-control col-12',
                    'placeholder' : 'fecha de nacimiento',
                    'type' : 'date'
                }
            ),

            'imagen' : forms.FileInput(
                attrs = {
                    'class':'form-control col-12',
                    'placeholder' : 'imagen'
                }
            ),

            'sexo' : forms.Select(
                attrs = {
                    'class':'form-control col-12',
                    'placeholder' : 'imagen'
                }
            ),

            'ciudad' : forms.Select(
                attrs = {
                    'class':'form-control col-12',
                    'placeholder' : 'asegurado'
                }
            ),

         
               'nacionalidad' : forms.Select(
                attrs = {
                    'class':'form-control col-12',
                    'placeholder' : 'asegurado'
                }
            ),


        }

#class MiembroForm(forms.ModelForm):
 #   class Meta:
  #     model = Suscripccion
   #     fields = ['correo','nombres','apellidos','sexo','documento','ciudad','nacionalidad','ciudad','fecha_nacimiento','imagen']


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

    #password2 = forms.CharField(label= 'confrimar password', required=True,
    #widget=forms.PasswordInput(attrs={
    #    'class' : 'form-control',
    #    'placeholder' : 'repita contraseña'

    #}))

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


    #def clean(self):
    #    cleaned_data = super().clean()
        
    #    if cleaned_data.get('password2') != cleaned_data.get('password'):
     #       self.add_error('password2','las contraseñas no coinciden')

class LoginForm(UserCreationForm):
    pass

#class LoginForm(AuthenticationForm):
#    def __init__(self, *args, **kwargs):
#        super(LoginForm,self).__init__(*args, **kwargs)
#        self.fields['username'].widget.attrs['class'] = 'form-control'
#        self.fields['username'].widget.attrs['placerholder'] = 'nombre de usuario'
#        self.fields['password'].widget.attrs['class'] = 'form-control'
#        self.fields['username'].widget.attrs['placerholder'] = 'contraseña'


