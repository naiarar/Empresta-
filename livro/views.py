from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuario
from .models import Emprestimo, Livros


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livros.objects.filter(usuario = usuario)
        return render(request, 'home.html', {'livros': livros})
    else:
        return redirect('/auth/login/?status=2')

def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        if request.session.get('usuario') == livros.usuario.id:
            return render(request, 'ver_livro.html', {'livro': livros})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')

def historico_emprestimos(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id = id)
        emprestimos = Emprestimo.objects.filter(livro = livros)
        if request.session.get('usuario') == livros.usuario.id:

            return render(request, 'historico_emprestimos.html', {'livro': livros, 'emprestimos': emprestimos})
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')
