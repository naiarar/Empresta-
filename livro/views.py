from curses.ascii import HT
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import redirect
from datetime import datetime
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
            'usuario': usuario,
            'status': request.GET.get('status')
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
        form = CadastroLivro(request.POST, request.FILES)

        if form.is_valid:
            form.save()
            return redirect('/livro/home')
        else:
            return HttpResponse('DADOS INVÁLIDOS')


def excluir_livro(request, id):
    livro = Livros.objects.get(id=id)
    if livro.usuario.id == request.session['usuario']:
        livro.delete()
        return redirect('/livro/home')
    else:
        return redirect('auth/sair')


def emprestar_livro(request, id):
    if request.method == 'POST':
        nome_emprestado = request.POST.get('nome_emprestado')
        id_livro_emprestado = id

        livro = Livros.objects.get(id=id_livro_emprestado)

    if livro.emprestado == False:
        emprestimo = Emprestimo(
            nome_emprestado_id=nome_emprestado,
            livro_id=id_livro_emprestado)

        emprestimo.save()
        livro.emprestado = True
        livro.save()

        return redirect('/livro/home/?status=10')
    else:

        return redirect('/livro/home/?status=1')


def devolver_livro(request, id):
    livro_devolver = Livros.objects.get(id=id)
    livro_devolver.emprestado = False
    livro_devolver.save()

    devolucao = Emprestimo.objects.filter(
        livro_id=id, data_devolucao=None).order_by('-data_emprestimo')[0]

    devolucao.data_devolucao = datetime.now()
    devolucao.save()

    return redirect('/livro/home/?status=11')


def seus_emprestimos(request):
    usuario = Usuario.objects.get(id=request.session['usuario'])
    emprestimos = Emprestimo.objects.filter(nome_emprestado=usuario)

    return render(request, 'seus_emprestimos.html', {'usuario_logado': request.session['usuario'],
                                                     'emprestimos': emprestimos})


def processa_avaliacao(request):
    id_emprestimo = request.POST.get('id_emprestimo')
    opcoes = request.POST.get('opcoes')
    id_livro = request.POST.get('id_livro')

    emprestimo = Emprestimo.objects.get(id=id_emprestimo)
    if emprestimo.livro.usuario.id == request.session['usuario']:
        emprestimo.avaliacao = opcoes
        emprestimo.save()
        print(id_livro)
        return redirect(f'/livro/ver_livro/{emprestimo.livro_id}')
    else:
        return HttpResponse('não')
