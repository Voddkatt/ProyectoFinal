from django import forms 
from django.forms import ModelForm
from .models import Clientes

class ClientesForm(ModelForm):

    class Meta: 
        model = Clientes
        fields =['cliente','usuario','producto','promociones','descuentos', 'categoria']