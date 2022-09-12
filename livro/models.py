from email import generator
from django.db import models
from uuid import uuid4
from datetime import datetime


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()
class Livros(models.Model):
    id_livro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    qnt_pag = models.IntegerField()
    editora = models.CharField(max_length=50)
    ano_publi = models.DateField(max_length=4)
    nota = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=50, blank=True, null=True)
    data_emprestimo = models.DateTimeField(blank=True, null=True)
    data_devolucao = models.DateTimeField(blank=True, null=True)

 

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.titulo






