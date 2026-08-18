from django.db import models


class Instrutor(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(
        max_length=14,
        unique=True
    )
    especialidade = models.CharField(
        max_length=100
    )
    cref = models.CharField(
        max_length=30,
        unique=True
    )
    ativo = models.BooleanField(
        default=True
    )
    def __str__(self):
        return self.nome