from django.db import models
from datetime import timedelta
from django.utils import timezone

from planos.models import Plano


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)

    data_matricula = models.DateField(default=timezone.localdate)
    data_vencimento = models.DateField(blank=True, null=True)

    ativo = models.BooleanField(default=True)

    plano = models.ForeignKey(
        Plano,
        on_delete=models.PROTECT,
        related_name="alunos"
    )

    def __str__(self):
        return self.nome