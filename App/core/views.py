from django.shortcuts import render
from .models import Productos

# Create your views here.

def index(request):

    datos = {
        'nombre': 'SuperAdmin', 
        'numero':[1,2,3]
    }

    return render(request,'core/home.html', datos)

def formulario(request):

    return render(request,'core/Formularios/Registro.html')

def login(request):

    return render(request, 'core/Formularios/Login.html')

def suscripcion(request):

    return render(request, 'core/Formularios/Suscripcion.html')

def productos(request):
    productos= Productos.objects.all()
    datos = {
        'productos': productos
    }
    return render(request, 'core/productos.html')

def form_productos(request):
    
    return render(request, 'core/form_productos.html')