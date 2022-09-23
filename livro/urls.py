from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('ver_livro/<int:id>', views.ver_livros, name = 'ver_livros' ),
    path('historico_emprestimos/<int:id>', views.historico_emprestimos, name = 'historico_emprestimos' ),
    path('cadastrar_livro', views.cadastrar_livro, name = 'cadastrar_livro'),
    path('excluir_livro/<int:id>', views.excluir_livro, name = 'excluir_livro'),
    path('emprestar_livro/<int:id>', views.emprestar_livro, name = 'emprestar_livro'),
    path('devolver_livro/<int:id>', views.devolver_livro, name = 'devolver_livro'),
    path('seus_emprestimos', views.seus_emprestimos, name = 'seus_emprestimos'),


]
