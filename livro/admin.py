from django.contrib import admin
from .models import Emprestimo, Livros, Categoria


admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Emprestimo)
