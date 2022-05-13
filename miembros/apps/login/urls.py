from django.urls import path, re_path
from .views import loginv,logoutnv,Register

urlpatterns = [
    path('log',loginv, name= 'log'),
    path('logout',logoutnv, name= 'logout'),
    path('registro',Register, name= 'registro'),
   
]
