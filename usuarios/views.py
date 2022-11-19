from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .models import Usuario



# Create your views here.
def login(request: HttpRequest):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status': status})


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=1')
    if len(senha.strip()) <= 8:
        return redirect('/auth/cadasstro/?status=2')
    usuario = Usuario.objects.filter(email=email).first()
    if usuario:
        return redirect('/auth/cadastro/?status=3')
    try:
        usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario.save()
        return redirect('/auth/login/?status=0')
    except e:  # pylint: disable=undefined-variable
        return redirect('/auth/cadastro/?status=4')


def valida_login(request: HttpRequest):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    if len(email.strip()) == 0:
        return redirect('/auth/login/?status=1')
    if len(senha.strip()) == 0:
        return redirect('/auth/login/?status=2')
    usuario = Usuario.objects.filter(email=email).first()
    if not usuario:
        return redirect('/auth/login/?status=3')
    if not Usuario.verificar_senha(usuario.senha, senha):
        return redirect('/auth/login/?status=3')

    request.session['usuario'] = usuario.id
    return redirect('/livro/home')


def sair(request: HttpRequest):
    request.session.flush()
    return redirect('/auth/login')
