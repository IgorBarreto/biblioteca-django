from datetime import datetime

from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from livro.models import Categoria, Emprestimo, Livros
from usuarios.models import Usuario

from .forms import CadastroLivro, CategoriaLivro


# Create your views here.
def home(request: HttpRequest):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        usuarios = Usuario.objects.all()
        status_categoria = request.GET.get('status_categoria')
        livros = Livros.objects.filter(usuario=usuario)
        total_livros = livros.count()
        livros_emprestar = Livros.objects.filter(usuario=usuario).filter(
            emprestado=False
        )
        livros_emprestados = Livros.objects.filter(usuario=usuario).filter(
            emprestado=True
        )
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(
            usuario=usuario
        )

        form_categoria = CategoriaLivro()
        return render(
            request,
            'home.html',
            {
                'livros': livros,
                'usuario_logado': request.session.get('usuario'),
                'form': form,
                'form_categoria': form_categoria,
                'status_categoria': status_categoria,
                'usuarios': usuarios,
                'livros_emprestar': livros_emprestar,
                'total_livros': total_livros,
                'livros_emprestados': livros_emprestados,
            },
        )
    return redirect('/auth/login/?status=4')


def detalhe_livro(request: HttpRequest, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)

        if request.session.get('usuario') == livro.usuario.id:
            categorias_livro = Categoria.objects.filter(
                usuario_id=request.session.get('usuario')
            )
            usuario = Usuario.objects.get(id=request.session['usuario'])
            usuarios = Usuario.objects.all()
            emprestimos = Emprestimo.objects.filter(livro=livro)
            livros = Livros.objects.filter(usuario=usuario)
            livros_emprestar = Livros.objects.filter(usuario=usuario).filter(
                emprestado=False
            )
            livros_emprestados = Livros.objects.filter(usuario=usuario).filter(
                emprestado=True
            )
            print(livros_emprestados)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(
                usuario=usuario
            )

            form_categoria = CategoriaLivro()

            return render(
                request,
                'detalhe_livro.html',
                {
                    'livro': livro,
                    'categorias_livro': categorias_livro,
                    'emprestimos': emprestimos,
                    'usuario_logado': request.session.get('usuario'),
                    'form': form,
                    'id_livro': id,
                    'usuarios': usuarios,
                    'form_categoria': form_categoria,
                    'livros': livros,
                    'livros_emprestar': livros_emprestar,
                    'livros_emprestados': livros_emprestados,
                },
            )
        else:
            return redirect('/auth/sair')
        return redirect('auth/login/?status=2')


def cadastrar_livro(request: HttpRequest):
    if request.method == 'POST':
        form = CadastroLivro(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/livro/home')
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)
        form = CadastroLivro()
        return render(
            request,
            'home.html',
            {
                'livros': livros,
                'usuario_logado': request.session['usuario'],
                'form': form,
            },
        )


def excluir_livro(request: HttpRequest, id):
    livro = Livros.objects.filter(id=id).first()
    if livro:
        livro.delete()
        return redirect('/livro/home')


def cadastrar_categoria(request: HttpRequest):
    form = CategoriaLivro(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario_logado')
    if int(id_usuario) == int(request.session.get('usuario')):
        categoria = Categoria(
            nome=nome,
            descricao=descricao,
            usuario_id=id_usuario,
        )
        categoria.save()
        return HttpResponseRedirect(next)
    return redirect('/livro/home/?status_categoria=1')


def cadastrar_emprestimo(request: HttpRequest):
    if request.method == 'POST':
        nome_emprestado = request.POST.get('nome_emprestado')
        nome_emprestado_anonimo = request.POST.get('nome_emprestado_anonimo')
        livro_emprestado = request.POST.get('livro_emprestado')
        next = request.POST.get('next', '/')
        if nome_emprestado_anonimo:
            emprestimo = Emprestimo(
                nome_emprestado_anonimo=nome_emprestado_anonimo,
                livro_id=livro_emprestado,
            )
        else:
            emprestimo = Emprestimo(
                nome_emprestado_id=nome_emprestado,
                livro_id=livro_emprestado,
            )
        emprestimo.save()
        livro = Livros.objects.get(id=livro_emprestado)
        livro.emprestado = True
        livro.save()
        return HttpResponseRedirect(next)


def devolver_livro(request):
    id = request.POST.get('id_livro_devolver')
    livro_devolver = Livros.objects.get(id=id)
    livro_devolver.emprestado = False

    emprestimo_devolver = Emprestimo.objects.get(
        Q(livro=livro_devolver) & Q(data_devolucao=None)
    )
    emprestimo_devolver.data_devolucao = datetime.now()
    emprestimo_devolver.save()
    return HttpResponseRedirect(next)


def atualizar_livro(request: HttpRequest):
    livro_id = request.POST.get('livro_id')
    nome_livro = request.POST.get('nome_livro')
    autor_livro = request.POST.get('autor_livro')
    co_autor_livro = request.POST.get('co_autor_livro')
    categoria_id = request.POST.get('categoria')
    categoria = Categoria.objects.get(id=categoria_id)
    livro = Livros.objects.get(id=livro_id)
    if livro.usuario == request.session.get['usuario']:
        livro.nome = nome_livro
        livro.autor = autor_livro
        livro.co_autor = co_autor_livro
        livro.categoria = categoria
        livro.save()
        return redirect(f'/livro/detalhe/{livro_id}')
    else:
        return redirect('/auth/sair')


def seus_emprestimos(request):
    usuario_logado = request.session['usuario']
    emprestimos = Emprestimo.objects.filter(nome_emprestado=usuario_logado)
    usuario = Usuario.objects.get(id=request.session['usuario'])
    livros_emprestados = Livros.objects.filter(usuario=usuario).filter(
        emprestado=True
    )
    usuarios = Usuario.objects.all()
    form_categoria = CategoriaLivro()
    livros_emprestar = Livros.objects.filter(usuario=usuario).filter(
        emprestado=False
    )

    form = CadastroLivro()
    form.fields['usuario'].initial = request.session['usuario']
    form.fields['categoria'].queryset = Categoria.objects.filter(
        usuario=usuario
    )
    return render(
        request,
        'seus_emprestimos.html',
        {
            'usuario_logado': usuario_logado,
            'emprestimos': emprestimos,
            'livros_emprestados': livros_emprestados,
            'form_categoria': form_categoria,
            'livros_emprestar': livros_emprestar,
            'form': form,
            'usuarios': usuarios,
        },
    )


def processa_avaliacao(request):
    id_emprestimo = request.POST.get('id_emprestimo')
    opcoes = request.POST.get('opcoes')
    next = request.POST.get('next', '/')
    emprestimo = Emprestimo.objects.get(id=id_emprestimo)
    if emprestimo.livro.usuario.id == request.session['usuario']:
        emprestimo.avaliacao = opcoes
        emprestimo.save()
        return HttpResponseRedirect(next)
    else:
        # TODO melhorar
        return HttpResponse('Esse emprestimo não é seu')
