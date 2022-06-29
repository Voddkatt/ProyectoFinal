from django.urls import path 
from .views import index ,formulario, login, suscripcion, clientes, form_clientes, form_mod_clientes, form_del_clientes, localizacion

urlpatterns = [
    path('', index, name="index"),
    path('formulario', formulario, name="form"),
    path('login', login, name="log"),
    path('suscripcion', suscripcion, name="sus"),
    path('clientes', clientes, name='client'),
    path('form-clientes', form_clientes, name="form_clientes"),
    path('form-mod-clientes/<id>' , form_mod_clientes, name="form_mod_clientes"),
    path('form-del_clientes/<id>', form_del_clientes, name="form_del_clientes"),
    path('localizacion', localizacion, name="local"),
]