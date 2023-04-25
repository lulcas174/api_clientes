from apps.clientes.models import Cliente
from apps.utils.utils import Utils


class ClienteRepository():

    def salvar_cliente(valores_request):
        utils = Utils()
        data_nascimento = utils.transformar_data_nascimento(valores_request['data_nascimento'])
        
        Cliente.objects.create(
            nome=valores_request['nome'],
            cpf=valores_request['cpf'],
            data_nascimento=data_nascimento,
        )

        return True
    
    def buscar_cliente(cpf):
        cliente = Cliente.objects.filter(cpf=cpf).first()

        return cliente