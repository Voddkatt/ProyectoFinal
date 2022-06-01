from django.shortcuts import render

# Create your views here.

def index(request):

    datos = {
        'nombre': 'SuperAdmin', 
        'numero':[1,2,3]
    }

    return render(request,'core/home.html',datos)

def formulario(request):

    return render(request,'core/Formularios/Registro.html')

    