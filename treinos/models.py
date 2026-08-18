from django.db import models

from alunos.models import Aluno
from funcionarios.models import Instrutor
from exercicios.models import Exercicio


class Treino(models.Model):
    nome = models.CharField(max_length=100)

    objetivo = models.CharField(
        max_length=150
    )

    descricao = models.TextField(
        blank=True
    )

    data_criacao = models.DateField(
        auto_now_add=True
    )

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="treinos"
    )

    instrutor = models.ForeignKey(
        Instrutor,
        on_delete=models.PROTECT,
        related_name="treinos"
    )

    exercicios = models.ManyToManyField(
        Exercicio,
        through="TreinoExercicio",
        related_name="treinos"
    )

    def __str__(self):
        return self.nome


class TreinoExercicio(models.Model):
    treino = models.ForeignKey(
        Treino,
        on_delete=models.CASCADE
    )

    exercicio = models.ForeignKey(
        Exercicio,
        on_delete=models.CASCADE
    )

    series = models.PositiveIntegerField(
        default=3
    )

    repeticoes = models.PositiveIntegerField(
        default=10
    )

    carga_kg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0
    )

    descanso_segundos = models.PositiveIntegerField(
        default=60
    )

    ordem = models.PositiveIntegerField(
        default=1
    )

    observacao = models.TextField(
        blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["treino", "exercicio"],
                name="treino_exercicio_unico"
            )
        ]

        ordering = ["ordem"]

    def __str__(self):
        return f"{self.treino} - {self.exercicio}"