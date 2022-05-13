from turtle import pu
from wsgiref.util import request_uri
from django import views
from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from django.http import  JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required, permission_required


from django.core.paginator import Paginator
from login.models import User
# Create your views here.

from suscripciones.models import Paciente
from login.models import Suscripccion


@login_required(login_url='log')
def MiembroApi(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('home')
    MAX_OBJECTS = 20
    miembros = User.objects.all() [:MAX_OBJECTS]
    data = {"results" : list(miembros.values("id","username","nombres","apellidos","sexo","documento","nacionalidad","ciudad","fecha_nacimiento","fecha_registro"))}
    return JsonResponse(data)


@login_required(login_url='log')
def MiembroDetalle(request, Id_User):
    poll = get_object_or_404(Suscripccion,Id_User = Id_User)
    data = {"results": {
        "correo" : poll.correo,
        "nombres" : poll.nombres,
        "apellidos" : poll.apellidos,
        "sexo" : poll.sexo,
        "documento" : poll.documento,
        "nacionalidad" : poll.nacionalidad,
        "ciudad" : poll.ciudad,
        "fecha_nacimiento" : poll.fecha_nacimiento,
        "fecha_registro" : poll.fecha_registro,
        "usuario_activo" : poll.usuario_activo
    }}

    return JsonResponse(data)

""" 
class ClientesApi(View):
    
    def get(self, request):
        lista = Suscripccion.objects.all()
        paginator = Paginator(lista, 50)
        page = request.GET.get('page')
        return JsonResponse(list(lista.values()), safe=False)
"""

class ClientesApidetalle(View):
    def get(self, request,Id_User):
        lista2 = Suscripccion.objects.get(Id_User=1)
        return JsonResponse(model_to_dict(lista2))

        
