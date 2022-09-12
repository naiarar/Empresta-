from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from usuarios.models import Usuario


def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        return HttpResponse(f'Bem vindo {usuario}')
    else:
        return redirect('/auth/login/?status=2')