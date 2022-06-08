from django.urls import path 
from .views import index ,formulario, login, suscripcion, productos, form_productos

urlpatterns = [
    path('', index, name="index"),
    path('formulario', formulario, name="form"),
    path('login', login, name="log"),
    path('suscripcion', suscripcion, name="sus"),
    path('productos', productos, name='prod'),
    path('form-productos', form_productos, name="form_productos"),
]