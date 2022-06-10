from django.shortcuts import render, redirect
from .models import *
from .forms import *

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
    return render(request, 'core/productos.html',datos)

def form_productos(request):
    
    datos = {
        'form': ProductosForm()
    }
    if request.method== 'POST':
        formulario = ProductosForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'

    return render(request, 'core/form_productos.html', datos)

def form_mod_productos(request, id):
    productos = Productos.objects.get(producto=id)
    datos = {
        'form': ProductosForm(instance=productos)
    }

    return render(request, 'core/form_mod_productos.html', datos)

def form_del_productos(request, id):
    productos = Productos.objects.get(producto=id)
    productos.delete()
    return redirect(to="productos")