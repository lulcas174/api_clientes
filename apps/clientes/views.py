from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from apps.clientes.models import Cliente
from apps.clientes.repository import ClienteRepository
from apps.clientes.serializers import ClientesSerializer
from apps.clientes.validators import Validador

class ClientesViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        validador = Validador()
        campos_validos_exceto_cpf = validador.validar_campos_exceto_cpf(request.data)

        if campos_validos_exceto_cpf and validador.validar_cpf(request.data['cpf']):
            ClienteRepository.salvar_cliente(request.data)
            return Response(
                "Cliente criado com sucesso",
                status=status.HTTP_201_CREATED
            )
        elif not validador.validar_cpf(request.data['cpf']):
            return Response(
                "CPF inválido",
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        else:
            return Response(
                "Campos inválidos",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        
    
    @action(detail=False, methods=["get"], url_path="buscar-cliente")
    def buscar_cliente(self, request):
        cliente = ClienteRepository.buscar_cliente(request.query_params['cpf'])
        if cliente:
            serializer = ClientesSerializer(cliente)
            
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        else:
            return Response(
                "Cliente não encontrado",
                status=status.HTTP_404_NOT_FOUND
            )
