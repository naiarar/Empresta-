from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('ver_livro/<int:id>', views.ver_livros, name = 'ver_livros' ),
    path('historico_emprestimos/<int:id>', views.historico_emprestimos, name = 'historico_emprestimos' ),

]
