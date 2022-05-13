from django.urls import path,re_path

from .views import ClientesApidetalle,MiembroApi,MiembroDetalle

urlpatterns = [
  path('miembros/', MiembroApi, name="amiembros"),
  path('per/<int:Id_User>/', MiembroDetalle, name="per"),
]