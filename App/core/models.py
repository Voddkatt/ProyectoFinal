from django.db import models

# Create your models here.
# Modelo para categoría de la florería 

class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='ID de categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoría')

    def __str__(self):
        return self.nombreCategoria

# Modelo para los productos de la florería 

class Productos(models.Model):
    producto = models.CharField(max_length=20, primary_key=True, verbose_name='Producto')
    flor = models.CharField(max_length=20, verbose_name='Tipo de flor')
    fertilizador = models.CharField(max_length=20, verbose_name='Tipo fertilizador')
    arbusto = models.CharField(max_length=20, verbose_name='Tipo arbusto')
    maceta = models.CharField(max_length=20, verbose_name='Tamaño maceta')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.producto 