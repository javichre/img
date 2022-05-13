from operator import itruediv
from tkinter.tix import Tree
from urllib import request
from urllib.request import Request
from email.mime.image import MIMEImage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail,send_mass_mail,EmailMultiAlternatives
from django.utils import timezone
from datetime import datetime,date
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
from django.template.loader import get_template
from django.db.models import Q

from login.models import Nacionalidad, Suscripccion,User
#from membrecias.suscripciones.models import Descuento
from suscripciones.models import Recibo,ReciboFormapago, Paciente, Orden, Emergencia, Admision

def Home(request):
    return render(request,'index.html')

def send_email(username):
    context = {'username':username}
    template = get_template('puntos/recordatorio.html')
    content = template.render(context)
    email = EmailMultiAlternatives (
        'Recuerde consumir sus puntos',
        'Socio MEDIRED',
        settings.EMAIL_HOST_USER,
        [username],
    )
    email.attach_alternative(content,'text/html')
    email.send()

@login_required(login_url='log')
def FiltroSexo(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')
    registrados = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()
    masculinos_porciento = (masculinos / registrados * 100)
    
@login_required(login_url='log')
def RegistradosPer(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    #registrados = User.objects.filter(fecha_registro = timezone.now())
    formapago = ReciboFormapago.objects.filter
    registrados = User.objects.all()
    mayores = timezone.now 

    #mayores  = User.objects.filter(nombres  2)
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))
    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))
    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    #username = request.POST.getlist("username") 
    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)

    #for i in correos:
    #    lista.append(i)
    
    #for i in lista:
        #correo = i

        #send_mail('Consumo de Puntos','Recuerde Consultas sus Puntos ','t3cn02018@gmail.com',[correo],fail_silently=False)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Masculino(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(sexo = "Masculino")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Femenino(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(sexo = "Femenino")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Otro(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')
        
    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)

    registrados = User.objects.filter(sexo = "Otro")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Membrecia(request):
    cedula = request.POST.get('cedula')
    nrecibos  = request.POST.getlist('idrecibo')
    #nrecibo = ReciboFormapago.objects.filter(formapagoid = 21 )
    usuario = request.user.documento
   
    registro = request.user.fecha_registro
    hoy = timezone.now()
    fecha_reistro = request.user.fecha_registro
    
    paso = Paciente.objects.filter(cedula = usuario)

    pasi = Paciente.objects.get (Q(cedula = usuario ) )

    recibo  = Orden.objects.filter(pacienteid  = pasi.pacienteid,estatus = 'PAG', descuento = 0, ) # fecha__gte=registro,fecha__lte=hoy,
    nrecibo = Orden.objects.filter(razonid_descuento = 16,estatus = 'PAG' ,pacienteid  = pasi.pacienteid, descuento__gte=0)

    paginator2  = Paginator(nrecibo,10)
    page2 = request.GET.get('page2')
    nrecibo = paginator2.get_page(page2)

    return render(request, 'registro/membrecia.html ', {'recibo':recibo,'usuario':usuario,
    'paso':paso,'nrecibos':nrecibos,'nrecibo':nrecibo,'pasi':pasi
    })

def Beneficios(request):
    return render(request,'miembros/beneficios.html')

def Requisitos(request):
    return render(request,'miembros/requisitos.html')

def Cobertura(request):
    return render(request,'miembros/cobertura.html')

@login_required(login_url='log')
def Filtro_Locales(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(nacionalidad = "Dominicana")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
    
    """ 
    correos = request.POST.getlist("correo")
    lista = []

    for i in correos:
        lista.append(i)
    
    for i in lista:
        correo = i

        send_mail('Consumo de Puntos','Recuerde Consultas sus Puntos ','t3cn02018@gmail.com',[correo],fail_silently=False)
    """
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Extranjeros(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(nacionalidad = "Extranjera")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Romana(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(ciudad = "Romana")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Romana(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(ciudad = "Romana")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
   
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Puntacana(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(ciudad = "Punta_Cana")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Bavaro(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(ciudad = "Bavaro")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Altagracia(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')
    registrados = User.objects.filter(ciudad = "Altagracia")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Seibo(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(ciudad = "Seibo")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Sanpedro(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(ciudad = "Sanpedro")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Hato_Mayor(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(ciudad = "Hato_Mayor")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))


    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def Filtro_Santo_Domingo(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')

    registrados = User.objects.filter(ciudad = "Santo_Domingo")
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))

    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))

    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))

    username  =  request.POST.getlist("username")
    if request.method == 'POST':
        for i in username:
            send_email(i)
  
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def FiltroMenos18(request):
    administrador = request.user.usuario_administrador
    if administrador == False:
        return redirect('miembro')
    
    edades = request.POST.getlist("edades") 
    #hoy = timezone.now()
    #hoy = datetime.today().strftime('%Y-%m-%d')
    hoy = date.today()
    for edad in edades:
        pass#print(edad)
    
    registrados = User.objects.all()

    for i in registrados:
        print(hoy - i.fecha_nacimiento )
    
    registrado = User.objects.all().count()
    masculinos = User.objects.filter(sexo = 'Masculino').count()
    femenino = User.objects.filter(sexo = 'Femenino').count()
    otro = User.objects.filter(sexo = 'Otro').count()

    masculinos_porciento = (masculinos / registrado * 100)
    masculinos_porciento = int(round(masculinos_porciento))
    femenino_porciento = (femenino / registrado * 100)
    femenino_porciento = int(round(femenino_porciento))
    otro_porciento = (otro / registrado * 100)
    otro_porciento = int(round(otro_porciento))
   
    return render(request, 'registro/listar_miembros.html',{'registrados':registrados,
    'registrado':registrado,'masculinos':masculinos,'femenino':femenino,'otro':otro,
    'masculinos_porciento':masculinos_porciento,'femenino_porciento':femenino_porciento,
    'otro_porciento':otro_porciento})

@login_required(login_url='log')
def actividad(request):
    
    miembros = User.objects.all()
    personas = Paciente.objects.all()

    for i in personas:
        for m in miembros:
            if(i.cedula == m.documento):
                print(i.pacienteid)
        #        break
    #for i in personas:
     #   for j in miembros:
      #      if(i.cedula==j.documento):
       #         print("aqui")
        #        break

    fecha_reistro = request.user.fecha_registro

    usuario = request.user.documento
    pasi = Paciente.objects.get (Q(  cedula = usuario ) | Q( cedula = 22500210202))
    recibo  = Recibo.objects.filter(pacienteid  = pasi.pacienteid,estatus = 'EMI' )
    return render(request,'actividad/actividad.html')

     #if(set(personas) == set(miembros)):
     #   print("Lists are equal")
    #else:
     #   print("Lists are not equal")