from django.db import models
from datetime import date


class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    data_nas = models.DateField(null=True, blank=False)
    cep = models.BigIntegerField(null=True, blank=False)
    rua = models.CharField(max_length=70, null=True, blank=False)
    numero = models.CharField(max_length=5, null=True, blank=False)
    complemento = models.CharField(max_length=15, null=True, blank=False)
    bairro = models.CharField(max_length=15, null=True, blank=False)
    cidade = models.CharField(max_length=15, null=True, blank=False)
    whatsapp = models.CharField(max_length=30, null=True, blank=False)
    instagram = models.CharField(max_length=30, null=True, blank=False)
    senha = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nome
