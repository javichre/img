from django.contrib import admin

from .models import Paciente, Recibo, Puntos
# Register your models her

admin.site.register(Recibo)
admin.site.register(Puntos)