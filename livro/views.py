from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuario
from .models import Emprestimo, Livros
from .forms import CadastroLivro


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']


        return render(request, 'home.html', {'livros': livros, 'usuario_logado': request.session.get('usuario'), 'form': form})
    else:
        return redirect('/auth/login/?status=2')


def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        form = CadastroLivro()
        if request.session.get('usuario') == livros.usuario.id:
            return render(request, 'ver_livro.html', {'livro': livros, 'usuario_logado': request.session.get('usuario'), 'form': form})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')


def historico_emprestimos(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        emprestimos = Emprestimo.objects.filter(livro=livros)
        if request.session.get('usuario') == livros.usuario.id:

            return render(request, 'historico_emprestimos.html', {'livro': livros, 'emprestimos': emprestimos})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')


def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse('Cadastro realizado com sucesso!')
        else:
            return HttpResponse('DADOS INVÁLIDOS')
        # livro = Livros
        # titulo = form.data['titulo']
        # autor = form.data['autor']
        # qnt_pag = form.data['qnt_pag']
        # editora = form.data['editora']
        # ano_publi = form.data['ano_publi']
        # nota = form.data['nota']
        # categoria = form.data['categoria']
