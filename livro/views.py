from curses.ascii import HT
from django.shortcuts import render, redirect
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

        conteudo = {
            'livros': livros,
            'usuario_logado': request.session.get('usuario'),
            'form': form,
            'usuario': usuario
        }

        return render(request, 'home.html', conteudo)
    else:
        return redirect('/auth/login/?status=2')


def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        form = CadastroLivro()

        usuarios = Usuario.objects.all()

        if request.session.get('usuario') == livros.usuario.id:
            return render(request, 'ver_livro.html', {'livro': livros,
                                                      'usuario_logado': request.session.get('usuario'),
                                                      'form': form,
                                                      'id_livro': id,
                                                      'usuarios': usuarios,
                                                      })
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
            return redirect('/livro/home')
        else:
            return HttpResponse('DADOS INVÁLIDOS')


def excluir_livro(request, id):
    livro = Livros.objects.get(id=id).delete()
    return redirect('/livro/home')


def emprestar_livro(request, id):
    if request.method == 'POST':
        nome_emprestado = request.POST.get('nome_emprestado')
        id_livro_emprestado = id

        livro = Livros.objects.get(id=id_livro_emprestado)

    if livro.emprestado == False:
            emprestimo = Emprestimo(
                nome_emprestado_id=nome_emprestado, livro_id=id_livro_emprestado)

            emprestimo.save()
            livro.emprestado = True
            livro.save()

            return HttpResponse('Emprestimo cadastrado com sucesso!')
    else:

            return HttpResponse('Desculpe, esse livro está emprestado')

