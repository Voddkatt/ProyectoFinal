from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Clientes
from .serializers import ClientesSerializer
@csrf_exempt
@api_view(['GET', 'POST'])
def lista_clientes(request):
    """
    Lista todos los clientes
    """
    if request.method == 'GET':
        clientes = Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClientesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
@api_view(['GET','PUT', 'DELETE'])
def detalle_clientes(request, id):
    #Get, update, o delte de un cliente en particular
    try:
        clientes = Clientes.objects.get(cliente=id)
    except Clientes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ClientesSerializer(clientes)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClientesSerializer(clientes, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        clientes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
