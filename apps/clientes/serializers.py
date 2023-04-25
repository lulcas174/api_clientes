from rest_framework.serializers import ModelSerializer

from apps.clientes.models import Cliente


class ClientesSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'