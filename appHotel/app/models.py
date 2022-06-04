from cProfile import label
from random import choices
from django.db import models
from pkg_resources import require


# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    cpf_cnpj = models.CharField(max_length=18, unique=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)


class TiposAcomodacao(models.Model):
    descricao = models.CharField(
        max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.descricao


class Acomodacao(models.Model):
    STATUS_CHOICES = {
        ('Em manutenção', 'Em manutenção'),
        ('Livre', 'Livre'),
        ('Ocupado', 'Ocupado'),
        ('Reservado', 'Reservado'),
    }
    unidade = models.IntegerField(
        unique=True, blank=False, null=False)
    tipo = models.ForeignKey(
        TiposAcomodacao, on_delete=models.PROTECT)
    andar = models.IntegerField(
        unique=False, blank=True, null=True)
    ramal = models.CharField(max_length=10, null=False,
                             blank=True)
    capacidade = models.IntegerField(
        unique=False, blank=False, null=True)
    valor = models.CharField(max_length=20, null=False, blank=True)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, null=False, blank=False)
    situacao = models.BooleanField()


class Diarias(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT)
    unidade = models.ForeignKey(
        Acomodacao, on_delete=models.PROTECT)
    hospedes = models.IntegerField(null=True, blank=True)
    entrada = models.DateField(null=True, blank=True)
    saida = models.DateField(null=True, blank=True)
    valor = models.FloatField(null=False, blank=False)
    adiantamento = models.FloatField(null=True, blank=True)
    observacao = models.TextField(null=True, blank=True)
