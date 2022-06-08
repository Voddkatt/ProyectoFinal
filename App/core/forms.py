from django import forms 
from django.forms import ModelForm
from .models import Productos

class ProductosForm(ModelForm):

    class Meta: 
        model = Productos 
        fields =['producto','flor','fertilizador','arbusto','maceta', 'categoria']