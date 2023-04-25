from django.forms import ValidationError
from datetime import date

from apps.utils.utils import Utils



class Validador():

    def __init__(self):
        self.utils = Utils()


    def validar_campos_exceto_cpf(self, valores_request):
        self.validar_nome(valores_request['nome'])
        self.validar_data_nascimento(valores_request['data_nascimento'])
        
        return True


    def validar_nome(self, nome):
        """
            Essa função vai receber o nome da pessoa via parâmetro.\n
            Vai primeiro validar o tamanho do nome.\n
            Depois vai validar se o nome não é vazio.\n
        """
        self.validar_tamanho_nome(nome)
        self.validar_nome_nao_vazio(nome)


    def validar_tamanho_nome(self, nome):
        """
            Essa função vai receber o nome da pessoa via parâmetro.\n
            Vai validar se o nome da pessoa tem mais de 3 caracteres.\n
            Vai validar se o nome da pessoa tem menos de 100 caracteres.\n
        """
        if len(nome) < 3:
            raise ValidationError('Nome deve ter mais de 3 caracteres')
        if len(nome) > 100:
            raise ValidationError('Nome deve ter menos de 100 caracteres')


    def validar_nome_nao_vazio(self, nome):
        """
            Essa função vai receber o nome da pessoa via parâmetro.\n
            Vai validar se o nome da pessoa não está vazio.\n
        """
        if nome == '':
            raise ValidationError('Nome não pode ser vazio')


    def validar_cpf(self, cpf):
        """
            Essa função vai receber o cpf da pessoa via parâmetro.\n
            Vai primeiro transformar o CPF da pessoa em digito.\n
            Depois vai validar o primeiro digito do CPF.\n
            Depois vai validar o segundo digito do CPF.\n
        """
        cpf_transformado = self.utils.transformar_cpf_validacao(cpf)
        return self.validar_primeiro_digito(cpf_transformado) == cpf_transformado[9] and \
            self.validar_segundo_digito(cpf_transformado) == cpf_transformado[10]


    def validar_primeiro_digito(self, cpf):
        """
            Essa função vai receber o cpf já transformado da pessoa via parâmetro.\n
            E vai validar os primeiros 9 dígitos do CPF.\n
        """
        soma = 0
        for i in range(10, 1, -1):
            soma += int(cpf[10 - i]) * i

        soma = (soma * 10) % 11
        if soma == 10:
            soma = 0

        return str(soma)


    def validar_segundo_digito(self, cpf):
        """
            Essa função vai receber o cpf já transformado da pessoa via parâmetro.\n
            E vai validar os primeiros 10 dígitos do CPF.\n
        """
        soma = 0
        for i in range(11, 1, -1):
            soma += int(cpf[11 - i]) * i

        soma = (soma * 10) % 11

        if soma == 10:
            soma = 0

        return str(soma)


    def validar_data_nascimento(self,data_nascimento):
        """
            Essa funcao vai receber a data de aniversario da pessoa via parametro.\n
            Vai primeiro transformar a data de aniversario da pessoa em digito.\n
            Depois vai validar se a data de aniversario não é maior que a data atual.\n
            Depois vai validar se a data de aniversario não é menor que a data atual.\n
        """
        data_atual = date.today()
        data_atual_convertida = self.utils.transformar_data_atual_brt(data_atual)
        data_nascimento_convertida = self.utils.transformar_data_nascimento(data_nascimento)
        self.validar_data_maior_atual(data_nascimento_convertida, data_atual_convertida)


    def validar_data_maior_atual(self, data_nascimento, data_atual):
        """
            Essa funcao vai receber a data de aniversario da pessoa via parametro e a data atual.\n
            Vai validar se a data de aniversario não é maior que a data atual.\n
        """
        if data_nascimento > data_atual:
            raise ValidationError('Data de aniversário não pode ser maior que a data atual')


