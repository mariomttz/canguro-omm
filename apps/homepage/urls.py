# Libraries and modules
from django.urls import path
from . import views

# URL's for the homepage app
urlpatterns = [
    path('',                views.inicio,         name='inicio'),
    path('registrarse/',    views.registrarse,    name='registrarse'),
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar-sesion'),
    path('cerrar-sesion/',  views.cerrar_sesion,  name='cerrar-sesion'),
    path('contacto/',       views.contacto,       name='contacto'),
]
