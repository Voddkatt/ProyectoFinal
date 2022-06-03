from django.db import models

# Create your models here.
# Modelo para categoría de la florería 

class Categoria(models.model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='ID de categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoría')

    def __str__(self):
        return self.nombreCategoria

# Modelo para los productos de la florería 

class Productos(models.Model):
    flores = models.CharField(max_length=20, primary_key=True, verbose_name='Flores')
    fertilizador = models.CharField(max_length=20, verbose_name='Tipo fertilizador')
    semilla
    maceta 
