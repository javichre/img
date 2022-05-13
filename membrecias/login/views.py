from csv import writer
import csv
from datetime import datetime
from distutils.log import Log


from multiprocessing import context
from operator import imod
from pyexpat import model

import csv
from urllib import request, response
from django import views

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from login.models import Nacionalidad
from django.utils import timezone
from suscripciones.models import Paciente,Recibo, Usuario
from django.core.paginator import Paginator
from django.views.generic import TemplateView,View,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template.loader import get_template


from .forms import LoginForm, MiembroForm,RegisterForm,LogForm
from suscripciones.models import ReciboFormapago,Recibo,Pacientes
from .models import User
#import urllib.request as urllib



def CreateUser(request):
    correo  = request.POST.get("username")
    #send_mail('Registro de Membrecia','Su registro Culmino Exitosamente','t3cn02018@gmail.com',[correo],fail_silently=False)

    if request.method == 'POST':
        createuser = LogForm(request.POST)
        if createuser.is_valid():
            createuser.save()
            return redirect('gracias')
    else:
        createuser = LogForm()
    
    return render(request, 'registro/registro.html', {'createuser': createuser} )

#############  #########################################################################

def send_email(username):
    context = {'username':username}
    template = get_template('registro/felicidades.html')
    content = template.render(context)

    email = EmailMultiAlternatives (
        'Registro de Membresia',
        'Socio MEDIRED',
        settings.EMAIL_HOST_USER,
        [username],
    )
    email.attach_alternative(content,'text/html')
    email.send()


class RegistraUsuario(CreateView):
    model = User
    form_class = LogForm
    template_name = 'registro/registro.html'
    #success_url = reverse_lazy('gracias')
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        username  = request.POST.get("username")
        if form.is_valid():
            send_email(username)
            form.save()
            return redirect('gracias')

        else:
            
            #messages.error(request, 'Las contraseñas no coinciden')
            return render(request, self.template_name, {'form':form} )

########################################################################################

def send_emaill(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        send_email(username)

    return render(request, 'correo.html', {})

def CreateMember(request):
    correo = queryset = request.POST.get("correo")
    send_mail('Registro de Membrecia','Su registro Culmino Exitosamente','t3cn02018@gmail.com',[correo],fail_silently=False)
    
    if request.method == 'POST':
        createmember = MiembroForm(request.POST)
        if createmember.is_valid():
            
            def Register(request):
                form = RegisterForm(request.POST or None)
                if request.method == 'POST' and form.is_valid():
                    username = form.cleaned_data.get('correo')
                    email = form.cleaned_data.get('correo')
                    password = form.cleaned_data.get('password')
                    user  = User.objects.create_user(username, email, password)
                    if user:
                        login(request, user)
                        messages.success(request, 'Usuario creando exitosamente')
                        return redirect('membrecia')
                return render(request, 'registro/registro.html' ,{'form': form} ) 

            createmember.save()
            return redirect('gracias')
    else:
        createmember = MiembroForm()
    
    return render(request,'registro/registro.html', {'createmember':createmember})

########################################################################################

def ListRecFomr(request,pacienteid):
    #pacientes = Pacientes.objects.filter(pacienteid = pacienteid)

    reciboform = Recibo.objects.filter(pacienteid = pacienteid)
    recibos = ReciboFormapago.objects.all()

    paginator  = Paginator(recibos,5)
    page = request.GET.get('page')
    recibos = paginator.get_page(page)
    paginator2 = Paginator(reciboform,10)
    page2 = request.GET.get('page2')
    reciboform = paginator2.get_page(page2)

    return render(request,'puntos/movimientos.html', {'recibos':recibos,'reciboform':reciboform} )

########################################################################################
"""
def RegisterUser(request):
    correo = queryset = request.POST.get("username")
    if request.method == 'POST':
        user = UserForm(request.POST)

        if user.is_valid():
            
            send_mail('Registro de Membrecia',
            'Su registro Culmino Exitosamente',
            't3cn02018@gmail.com',
            [correo],fail_silently=False)


            ##### esta funcion sirve para al mismo tiempo que se registre una persona registrar el login de una personas
            def Register(request):
                form = RegisterForm(request.POST or None)
                if request.method == 'POST' and form.is_valid():
                    username = form.cleaned_data.get('username')
                    email = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user  = User.objects.create_user(username, email, password)
                    if user:
                     login(request, user)
                     messages.success(request, 'Usuario creando exitosamente')
                     return redirect('membrecia')
            
                return render(request, 'registro/registro.html' ,{
                    'form': form
                } )
            user.save()
            messages.success(request,'Usuario Registrado Exitosamente')
            return redirect('gracias')
    else:
        user = UserForm()
        messages.error(request,'No se puedo Registrar el Usuario')

    return render(request,'registro/registro.html', {'user':user} )

"""

########################################################################################

def lisper(request):
    usuarios = prueba.objects.all()
    paginator = Paginator(usuarios, 50)
    page = request.GET.get('page')
    usuarios = paginator.get_page(page)
    return render(request,'registro/listar_miembros.html', {'usuarios':usuarios} )

########################################################################################

def ListUser(request):
    usuarios = prueba.objects.all()
    paginator = Paginator(usuarios, 50)
    page = request.GET.get('page')
    usuarios = paginator.get_page(page)
    return render(request,'registro/listar_miembros.html', {'usuarios':usuarios} )

########################################################################################

def ListClient(request):
    usuarios = User.objects.all()
    paginator = Paginator(usuarios, 50)
    page = request.GET.get('page')
    usuarios = paginator.get_page(page)
    return render(request,'registro/listar_miembros.html', {'usuarios':usuarios} )

########################################################################################

def ListRecibo(request,pacienteid):
    recibos = Recibo.objects.filter(pacienteid = pacienteid)
    reciboss = Recibo.objects.all()
    paginator = Paginator(recibos, 50)
    page = request.GET.get('page')
    recibos = paginator.get_page(page)

    for i in recibos:
        pass
    return render(request,'puntos/movimientos.html', {'recibos':recibos} )

########################################################################################

class Login(FormView):
    template_name = 'login/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('gracias')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request, *args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

########################################################################################

class LoginView(TemplateView):
    template_name = "login/login.html"
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username,password= password)

        if user is not None:
            login(request,user)
            return redirect('gracias')
        return render(
            request, "login/login.html",{
                "error" : "Contraseña o usuario incorrecto"})
########################################################################################

def Gracias(request):
    return render(request,'registro/gracias.html')

################## ESTA USO PARA EL LOGIN###############################################

class loginv(TemplateView):
   
    template_name = "login/login.html"
    def post(self, request, *args, **kwargs):
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password =password)
        if user is not None:
            login(request, user)
            return redirect('miembro')
        
        return render(
            request,  "login/login.html" , {
                "error" : "Usuario o Contraseña Incorrecta"

            }
        )

########################################################################################

def Logout(request):
    logout(request)
    return redirect('log')

def export_csv(request):
    response = HttpResponse(content_type = 'text/xls')
    response['Content-Disposition'] = 'attachment; filename=Expenses'+  '.xls'
    
    
    writer=csv.writer(response)
    writer.writerow(['Usuario','Nombres','Apellidos','Sexo','Documento','Nacionalidad','Ciudad','Telefono'])

    expenses=User.objects.all()

    for expense in expenses:
        writer.writerow([expense.username, expense.nombres, expense.apellidos, expense.sexo, expense.documento, expense.nacionalidad, expense.ciudad, expense.telefono])
    
    return response