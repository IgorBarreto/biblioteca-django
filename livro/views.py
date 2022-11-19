from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from usuarios.models import Usuario


# Create your views here.
def home(request: HttpRequest):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        return HttpResponse(f'Seja bem vindo(a) {usuario.nome}')
    return redirect('/auth/login/?status=4')
