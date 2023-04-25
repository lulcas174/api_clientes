from datetime import datetime

class Utils():

    def transformar_cpf_validacao(self, cpf):
        """
            Essa funcao vai receber o cpf da pessoa via parametro.\n
            Vai primeiro transformar o CPF da pessoa em digito.\n
        """
        cpf_numerico = ''.join(filter(str.isdigit, cpf))
        return cpf_numerico
    

    def transformar_data_nascimento(self, data_nascimento):
        try:
            data_nascimento_objeto = datetime.strptime(data_nascimento, '%d%m%Y')
        except:
            data_nascimento_objeto = datetime.strptime(data_nascimento, '%d/%m/%Y')

        data_formatada = data_nascimento_objeto.strftime('%d/%m/%Y')

        return data_formatada

    
    def transformar_data_atual_brt(self, data_atual):
        data_atual = datetime.now()
        data_formatada = data_atual.strftime('%d/%m/%Y')

        return data_formatada