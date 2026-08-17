from django.db import models
from django.utils import timezone
from datetime import timedelta


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_dias = models.PositiveIntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


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
                self.data_matricula +
                timedelta(days=self.plano.duracao_dias)
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Instrutor(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)

    especialidade = models.CharField(max_length=100)

    cref = models.CharField(
        max_length=30,
        unique=True
    )

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)

    descricao = models.TextField(blank=True)

    grupo_muscular = models.CharField(
        max_length=100
    )

    equipamento = models.CharField(
        max_length=100,
        blank=True
    )

    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Treino(models.Model):
    nome = models.CharField(max_length=100)

    objetivo = models.CharField(
        max_length=150
    )

    descricao = models.TextField(blank=True)

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
        unique_together = (
            "treino",
            "exercicio"
        )

        ordering = ["ordem"]

    def __str__(self):
        return f"{self.treino} - {self.exercicio}"