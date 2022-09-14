from email import generator
from django.db import models
from uuid import uuid4
from datetime import datetime
from usuarios.models import Usuario


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome

class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    qnt_pag = models.IntegerField()
    editora = models.CharField(max_length=50)
    ano_publi = models.CharField(max_length=10)
    nota = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    emprestado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.titulo


 
class Emprestimo(models.Model):
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    data_emprestimo = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.nome_emprestado} | {self.livro}'





