from django import forms
from django.db.models import fields
from .models import Livros


class CadastroLivro(forms.ModelForm):
    class Meta: 
        model = Livros
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()



