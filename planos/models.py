from django.db import models


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_dias = models.PositiveIntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome