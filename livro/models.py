from email import generator
from django.db import models
from uuid import uuid4

class Livros(models.Model):
    id_livro = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    qnt_pag = models.IntegerField()
    editora = models.CharField(max_length=50)
    ano_publi = models.DateField(max_length=4)
    nota = models.IntegerField(max_length=2)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=50)
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    




