## Como rodar aplicação local.
- Primeiro passo é fazer o setup do seu .env
    - O exemplo de como deve ser o .env está no ".env-example"
- O python precisa estar na versão: ```Python 3.10.2```
    - Caso não tenha um gerenciador de versões de python, recomendo o [pyenv](https://github.com/pyenv/pyenv)
- Você precisa criar um ambiente virtual do python e ativa-lo
- Após configurado o .env você precisa rodar o comando ```pip install -r requirements.txt```
- Após isso você precisa rodar o comando ```python manage.py migrate```
- Com isso você só precisa rodar o servidor e já está pronta
