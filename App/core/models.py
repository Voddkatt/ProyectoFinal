from django.db import models

# Create your models here.
# Modelo para categoría de la florería 

class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='ID de categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoría')

    def __str__(self):
        return self.nombreCategoria

# Modelo para los productos de la florería 

class Clientes(models.Model):
    cliente = models.CharField(max_length=20, primary_key=True, verbose_name='Cliente')
    usuario = models.CharField(max_length=20, verbose_name='Usuario')
    producto = models.CharField(max_length=20, verbose_name='Productos')
    promociones = models.CharField(max_length=20, verbose_name='Promociones')
    descuentos = models.CharField(max_length=20, verbose_name='Descuentos')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.cliente