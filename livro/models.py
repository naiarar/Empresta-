from django.db import models    
from datetime import date
import datetime
from django.db.models.base import Model
from usuarios.models import Usuario



class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    def __str__(self) -> str:
        return self.nome

class Livros(models.Model):
    image = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    qnt_pag = models.IntegerField()
    editora = models.CharField(max_length=50)
    ano_publi = models.CharField(max_length=10)
    nota = models.IntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    emprestado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.titulo


 
class Emprestimo(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank = True, null = True)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now())
    data_devolucao = models.DateTimeField(blank = True, null = True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nome_emprestado} | {self.livro}"

