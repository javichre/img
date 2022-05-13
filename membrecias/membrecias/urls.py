
from django.contrib import admin
from django.urls import path, include


from suscripciones.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('membrecias/', include('login.urls')),
    path('api/', include('clientesapi.urls')),
    path('memberchip/', include('suscripciones.urls')),
]
