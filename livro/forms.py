from django import forms
from django.db.models import fields
from .models import Livros


class CadastroLivro(forms.ModelForm):
    class Meta: 
        model = Livros
        fields = ('titulo', 'autor', 'qnt_pag', 'editora', 'ano_publi', 'nota', 'categoria', 'usuario')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



