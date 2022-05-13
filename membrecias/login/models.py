from distutils.command.upload import upload
import imp
from locale import normalize
from multiprocessing.sharedctypes import Value
from operator import truediv
from datetime import date, datetime
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from typing import Tuple
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.



from suscripciones.models import Paciente
""" 
class prueba(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    paciente = models.ForeignKey(Paciente,on_delete=models.CASCADE)
"""
class sexo(models.Model):
    Id_Sexo = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.sexo

class Ciudad(models.Model):
    Id_Ciudad = models.AutoField(primary_key=True)
    ciudad  = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        ordering = ['ciudad']

    def __str__(self):
        return self.ciudad

class EstadoCivil(models.Model):
    Id_estadocivil = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.descripcion

class Nacionalidad(models.Model):
    Id_Nacionalidad = models.AutoField(primary_key=True)
    nacionalidad = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.nacionalidad

class ManagerUser(BaseUserManager):
    def create_user(self,username,nombres,apellidos,sexo,documento,nacionalidad,ciudad,fecha_nacimiento,telefono,password = None):
        if not username:
            raise ValueError('Debe Ingresar un correo')
        
        usuario = self.model(username = self.normalize_email(username),
        nombres = nombres,
        apellidos = apellidos,
        sexo=sexo,
        documento=documento,
        nacionalidad = nacionalidad,
        ciudad = ciudad,
        fecha_nacimiento = fecha_nacimiento,
        telefono = telefono
        )

        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, username, nombres,apellidos,sexo,documento,nacionalidad,ciudad,fecha_nacimiento,telefono,password):
        usuario = self.create_user(
            username,
            nombres=nombres,
            apellidos=apellidos,
            sexo=sexo,
            documento=documento,
            nacionalidad=nacionalidad,
            ciudad=ciudad,
            fecha_nacimiento=fecha_nacimiento,
            telefono=telefono,
            password=password


        )

        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class User(AbstractBaseUser):
    username = models.EmailField(null=False, blank=False,unique=True)
    nombres = models.CharField(max_length=100, null=False,blank=False)
    apellidos = models.CharField(max_length=100,null=False,blank=False)
    sexo = models.CharField(max_length=50, null=True, blank=True)
    documento = models.CharField('Documento', blank=True,null=True, max_length=15)
    nacionalidad = models.CharField(max_length=100, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha Naci,iento',null=False,blank=False)
    telefono = models.BigIntegerField(blank=True, null=True)
    imagen = models.ImageField('Imagen de Perfil',upload_to="perfil/", null= True,blank = True, height_field=None, width_field=None,max_length=200 )
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = ManagerUser()

    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['nombres','apellidos','sexo','documento','nacionalidad','ciudad','fecha_nacimiento']

    def calcular_edad(self):
        return date.today().year - self.fecha_nacimiento.year

    def __str__(self):
        return self.username
        #return f'{self.nombres},{self.apellidos}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador
         
class Suscripccion(models.Model):
    Id_User = models.AutoField(primary_key=True)
    correo = models.EmailField('Correo Electronico', unique=True,max_length=100)
    nombres  = models.CharField('Nombres',max_length=100, null=False,blank=False)
    apellidos = models.CharField('Apellidos',max_length=100, null=False, blank=False)
    sexo = models.ForeignKey(sexo,on_delete=models.CASCADE)
    documento = models.BigIntegerField('Documento',  blank=True,null=True,unique=True)
    #estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE)
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    #documento_responsable = models.CharField('Documento Persona Responsable',max_length=20, blank=True,null=True)
    fecha_nacimiento = models.DateField('Fecha Naci,iento',null=False,blank=False)
    imagen = models.ImageField('Imagen de Perfil',upload_to="perfil/", null= True,blank = True, height_field=None, width_field=None,max_length=200 )

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

class Puntos(models.Model):
    IdPuntos = models.AutoField(primary_key=True)
    puntos = models.FloatField()

##############################################################################################

class Paciente(models.Model):
    pacienteid = models.AutoField(primary_key=True)
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    nombres = models.CharField(max_length=80, blank=True, null=True)
    sexoid = models.IntegerField(blank=True, null=True)
    estadocivilid = models.IntegerField(blank=True, null=True)
    medicoid = models.IntegerField(blank=True, null=True)
    sangreid = models.IntegerField(blank=True, null=True)
    razaid = models.IntegerField(blank=True, null=True)
    seguroid = models.IntegerField(blank=True, null=True)
    paisid = models.IntegerField(blank=True, null=True)
    planid = models.IntegerField(blank=True, null=True)
    profesionid = models.IntegerField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_nac = models.DateTimeField(blank=True, null=True)
    fecha_fellecio = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    motivo_fellecio = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    foto = models.CharField(max_length=100, blank=True, null=True)
    poliza = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    celular = models.CharField(max_length=30, blank=True, null=True)
    cedula = models.CharField(max_length=13, blank=True, null=True)
    pasaporte = models.CharField(max_length=20, blank=True, null=True)
    apodo = models.CharField(max_length=20, blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    fallecido = models.CharField(max_length=5, blank=True, null=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tipopacienteid = models.IntegerField(blank=True, null=True)
    nss = models.CharField(max_length=50, blank=True, null=True)
    web_usuario = models.CharField(max_length=50, blank=True, null=True)
    web_clave = models.CharField(max_length=50, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)
    alergias = models.TextField(blank=True, null=True)  # This field type is a guess.
    vacunas = models.TextField(blank=True, null=True)  # This field type is a guess.
    antecedentes = models.TextField(blank=True, null=True)  # This field type is a guess.
    tratamiento = models.TextField(blank=True, null=True)  # This field type is a guess.
    cirugias = models.TextField(blank=True, null=True)  # This field type is a guess.
    cronicas = models.TextField(blank=True, null=True)  # This field type is a guess.
    habitos_personales = models.TextField(blank=True, null=True)  # This field type is a guess.
    estatus = models.CharField(max_length=3, blank=True, null=True)
    trabajo_telefono = models.CharField(max_length=20, blank=True, null=True)
    trabajo_nombre = models.CharField(max_length=100, blank=True, null=True)
    vip = models.IntegerField(blank=True, null=True)
    antecedentes_familiares = models.TextField(blank=True, null=True)  # This field type is a guess.
    no_grato = models.IntegerField(blank=True, null=True)
    vip_mensaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    nograto_mensaje = models.TextField(blank=True, null=True)  # This field type is a guess.
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    gestion_cobro = models.IntegerField(blank=True, null=True)
    usuarioid_modifica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'


    opcfacturaid = models.IntegerField(blank=True, null=True)
    facturaintid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente_archivo'

class Recibo(models.Model):
    reciboid = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    conceptoid = models.IntegerField(blank=True, null=True)
    emergenciaid = models.IntegerField(blank=True, null=True)
    ordenid = models.IntegerField(blank=True, null=True)
    admisionid = models.IntegerField(blank=True, null=True)
    usuarioid = models.IntegerField(blank=True, null=True)
    turnoid = models.IntegerField(blank=True, null=True)
    tiponcfid = models.IntegerField(blank=True, null=True)
    pacienteid = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    seguroid = models.IntegerField(blank=True, null=True)
    estatus = models.CharField(max_length=3, blank=True, null=True)
    monto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    rnc = models.CharField(max_length=11, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    medicoid = models.IntegerField(blank=True, null=True)
    razonid = models.IntegerField(blank=True, null=True)
    ncf_nombre = models.CharField(max_length=200, blank=True, null=True)
    facturaid = models.IntegerField(blank=True, null=True)
    hora = models.DateTimeField(blank=True, null=True)
    clienteid = models.IntegerField(blank=True, null=True)
    cuadrada = models.IntegerField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    usuarioid_anula = models.IntegerField(blank=True, null=True)
    monedaid = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    cierreid = models.IntegerField(blank=True, null=True)
    nota_anulacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    admisionid_honorario = models.IntegerField(blank=True, null=True)
    sucursalid = models.IntegerField(blank=True, null=True)
    retencion = models.DecimalField(max_digits=18, decimal_places=2)
    puntos = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibo'

class ReciboFactura(models.Model):
    reciboid = models.IntegerField(primary_key=True)
    facturaid = models.IntegerField()
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_fecha = models.DateTimeField(blank=True, null=True)
    factura_vence = models.DateTimeField(blank=True, null=True)
    factura_monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_pagado = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_pendiente = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_int = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_amb = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_eme = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    objecion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    ncf = models.CharField(max_length=20, blank=True, null=True)
    glosa_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    objecion_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    factura_cafeteria = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    factura_nd = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    factura_prod = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    opcfacturaid = models.IntegerField(blank=True, null=True)
    numero = models.CharField(max_length=30, blank=True, null=True)
    retencion = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'recibo_factura'
        unique_together = (('reciboid', 'facturaid'),)

class ReciboFacturaDetalle(models.Model):
    reciboid = models.IntegerField(primary_key=True)
    facturaid = models.IntegerField()
    detalleid = models.IntegerField()
    tipo = models.CharField(max_length=3, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    autorizacion = models.CharField(max_length=50, blank=True, null=True)
    poliza = models.CharField(max_length=30, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    cobertura = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    objecion = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    glosa = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    objecion_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    glosa_nota = models.TextField(blank=True, null=True)  # This field type is a guess.
    pacienteid = models.IntegerField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    retencion = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'recibo_factura_detalle'
        unique_together = (('reciboid', 'facturaid', 'detalleid'),)

class ReciboFormapago(models.Model):
    reciboid = models.ForeignKey(Recibo, on_delete=models.CASCADE)
    detalleid = models.IntegerField()
    formapagoid = models.IntegerField(blank=True, null=True)
    bancoid = models.IntegerField(blank=True, null=True)
    monto = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tarjeta = models.CharField(max_length=16, blank=True, null=True)
    cheque = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    credito_empleado = models.IntegerField(blank=True, null=True)
    credito_cliente = models.IntegerField(blank=True, null=True)
    transaccionid = models.IntegerField(blank=True, null=True)
    autorizacion = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recibo_formapago'
        unique_together = (('reciboid', 'detalleid'),)

class PuntosAcu(models.Model):
    paciente  = models.BigIntegerField(null=True, blank=True)
    Puntos  = models.BigIntegerField(null=True, blank=True)
    cedula = models.CharField(null=True, blank=True,max_length=15)

    def __str__(self):
        return self.paciente