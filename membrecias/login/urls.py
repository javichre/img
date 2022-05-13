import imp
from lib2to3.pgen2 import grammar
from unicodedata import name
from django import views
from django.contrib.auth import login
from django.urls import path, re_path
from .views import ListUser,ListClient, ListRecibo,LoginView,Gracias,Login,loginv,ListRecFomr,CreateMember,CreateUser,RegistraUsuario,Logout,export_csv


# {'redirect_if_logged_in': 'miembro'}
urlpatterns = [
  
   path('listar',ListUser, name= 'listar'),
   path('listarc',ListClient, name= 'listarc'),
   path('listarr/<int:pacienteid>',ListRecibo, name= 'listarr'),
   path('',login, {'template_name': 'login/login.html'}, name='login' ),
   path('gracias',Gracias, name= 'gracias'),
   path('cuenta',Login.as_view(), name= 'cuenta'),
   path('log',loginv.as_view(), name= 'log'  ),
   path('mm/<int:pacienteid>',ListRecFomr, name= 'mm'),
   path('registrar',CreateMember, name= 'registrar'),
   path('registro/',CreateUser, name= 'registro'),
   path('register/',RegistraUsuario.as_view(), name= 'register'),
   path('logout/',Logout, name= 'logout'),
   path('export/',export_csv, name= 'export'),

   
  
 
]


   # nuevo_usuario = Usuario(
            #    username = form.cleaned_data.get('username'),
             #   nombres = form.cleaned_data.get('nombres'),
              #  apellidos = form.cleaned_data.get('apellidos'),
               # sexo = form.cleaned_data.get('sexo'),
                #documento = form.cleaned_data.get('documento'),
                #nacionalidad = form.cleaned_data.get('nacionalidad'),
                #ciudad = form.cleaned_data.get('ciudad'),
                #fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento'),
            #)
            #nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            #nuevo_usuario.save()