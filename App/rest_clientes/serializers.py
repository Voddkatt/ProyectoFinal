from rest_framework import serializers
from core.models import Clientes
class ClientesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Clientes
        fields =['cliente','usuario','producto','promociones','descuentos', 'categoria']
