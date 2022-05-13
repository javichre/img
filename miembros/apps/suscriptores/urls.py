from django.urls import path, re_path
from .views import Memberchip
urlpatterns = [
   path('membrecia',Memberchip, name= 'membrecia'),
]
