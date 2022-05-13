from operator import imod
from re import template
import re
from urllib import request
from django import views
import django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy

from django.core.paginator import Paginator
from django.views.generic import TemplateView,View
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from django.views.decorators.csrf import csrf_protect 

from .forms import RegisterForm


def loginv(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request,'Bienvenido {} '.format(user.username) )
            return redirect ('membrecia')
        
        else:
            messages.error(request, 'Usuario o Contraseña no validos')
        

    return render(request,  "login/login.html" ,{

    } )

def logoutnv(request):
    logout(request)
    messages.success(request , 'Sesion cerrada exitosamente')
    return redirect('log')


def Register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user  = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creando exitosamente')
            return redirect('membrecia')

    


    return render(request, 'registro/registro.html' ,{
        'form': form
    } )

