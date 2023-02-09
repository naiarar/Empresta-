from django.db import models
from datetime import date


class Usuario(models.Model):
    # nome = models.CharField(max_length=30)
    # email = models.EmailField(null=True, blank=True)
    # senha = models.CharField(max_length=10, null=True, blank=True)

    nome = models.CharField(max_length=10)
    email = models.EmailField()
    senha = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.nome
