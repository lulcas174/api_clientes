from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.clientes.models import Cliente
from apps.clientes.serializers import ClientesSerializer


class ClientesViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)