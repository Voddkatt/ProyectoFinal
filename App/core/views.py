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

def clientes(request):
    clientes= Clientes.objects.all()
    datos = {
        'clientes': clientes
    }
    return render(request, 'core/clientes.html',datos)

def form_clientes(request):
    
    datos = {
        'form': ClientesForm()
    }
    if request.method== 'POST':
        formulario = ClientesForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'

    return render(request, 'core/form_clientes.html', datos)

def form_mod_clientes(request, id):
    clientes = Clientes.objects.get(cliente=id)
    datos = {
        'form': ClientesForm(instance=clientes)
    }

    return render(request, 'core/form_mod_clientes.html', datos)

def form_del_clientes(request, id):
    clientes = Clientes.objects.get(cliente=id)
    clientes.delete()
    return redirect(to="clientes")

def localizacion(request):

    return render(request, 'core/localizacion.html')
    