from django.db import models
from datetime import timedelta
from django.utils import timezone

from planos.models import Plano


class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    data_matricula = models.DateField(default=timezone.localdate)
    data_vencimento = models.DateField(blank=True, null=True)

    ativo = models.BooleanField(default=True)

    plano = models.ForeignKey(
        Plano,
        on_delete=models.PROTECT,
        related_name="alunos"
    )

    def save(self, *args, **kwargs):
        if self.plano and self.data_matricula:
            self.data_vencimento = (
                self.data_matricula
                + timedelta(days=self.plano.duracao_dias)
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome