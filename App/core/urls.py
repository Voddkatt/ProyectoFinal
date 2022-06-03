from django.urls import path 
from .views import index ,formulario, login, suscripcion

urlpatterns = [
    path('', index, name="index"),
    path('formulario', formulario, name="form"),
    path('login', login, name="log"),
    path('suscripcion', suscripcion, name="sus"),
]