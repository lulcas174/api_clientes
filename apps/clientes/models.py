from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    data_nascimento = models.CharField(max_length=12)