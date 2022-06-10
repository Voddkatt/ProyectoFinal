from django.urls import path 
from .views import index ,formulario, login, suscripcion, productos, form_productos, form_mod_productos, form_del_productos

urlpatterns = [
    path('', index, name="index"),
    path('formulario', formulario, name="form"),
    path('login', login, name="log"),
    path('suscripcion', suscripcion, name="sus"),
    path('productos', productos, name='prod'),
    path('form-productos', form_productos, name="form_productos"),
    path('form-mod-productos/<id>' , form_mod_productos, name="form_mod_productos"),
    path('form-del_productos/<id>', form_del_productos, name="form_del_productos"),
]