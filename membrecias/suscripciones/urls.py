from django.urls import path,re_path
from django.shortcuts import redirect, render
from .views import Filtro_Romana, Membrecia
from .views import RegistradosPer,Beneficios,Filtro_Masculino,Filtro_Femenino,Filtro_Otro,Requisitos,Cobertura,Filtro_Locales,Filtro_Extranjeros,Filtro_Romana,Filtro_Puntacana,Filtro_Bavaro,Filtro_Altagracia,Filtro_Seibo,Filtro_Sanpedro,Filtro_Hato_Mayor,Filtro_Santo_Domingo,actividad,FiltroMenos18


urlpatterns = [
      path('miembro/', Membrecia, name="miembro"),
      path('miembros/', RegistradosPer, name="miembros"),
      path('beneficios/', Beneficios, name="beneficios"),
      path('masculino/', Filtro_Masculino, name="masculino"),
      path('femenino/', Filtro_Femenino, name="femenino"),
      path('otro/', Filtro_Otro, name="otro"),
      path('cobertura/', Cobertura, name="cobertura"),
      path('requisitos/', Requisitos, name="requisitos"),
      path('dominicanos/', Filtro_Locales, name="dominicanos"),
      path('extranjeros/', Filtro_Extranjeros, name="extranjeros"),
      path('romana/', Filtro_Romana, name="romana"),
      path('puntacana/', Filtro_Puntacana, name="puntacana"),
      path('bavaro/', Filtro_Bavaro, name="bavaro"),
      path('altagracia/', Filtro_Altagracia, name="altagracia"),
      path('seibo/', Filtro_Seibo, name="seibo"),
      path('sanpedro/', Filtro_Sanpedro, name="sanpedro"),
      path('hatomayor/', Filtro_Hato_Mayor, name="hatomayor"),
      path('santodomingo/', Filtro_Santo_Domingo, name="santodomingo"),
      path('actividad/', actividad, name="actividad"),
      path('mas18/', FiltroMenos18, name="mas18"),


      
]
