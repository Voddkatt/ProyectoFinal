from django.urls import path 
from .views import index ,formulario

urlpatterns = [
    path('', index, name="index"),
    path('formulario', formulario, name="form"),
]