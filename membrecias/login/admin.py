import imp
from pyexpat import model
from re import search
from django.contrib import admin
from .models import sexo, Ciudad, Nacionalidad, Puntos, Suscripccion, Recibo, Paciente, ReciboFormapago,User,PuntosAcu
from import_export import resources 
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class MiembrosResources(resources.ModelResource):
    class Meta:

        model = User


class MiembrosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['documento']
    list_display = ('nombres','apellidos','ciudad')
    resource_class = MiembrosResources


admin.site.register(sexo)
admin.site.register(Ciudad)
admin.site.register(Nacionalidad)
admin.site.register(Puntos)
admin.site.register(Suscripccion)
admin.site.register(Recibo)
admin.site.register(Paciente)
admin.site.register(ReciboFormapago)
admin.site.register(User,MiembrosAdmin)
admin.site.register(PuntosAcu)


