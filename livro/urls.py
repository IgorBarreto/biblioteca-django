from django.urls import path

from . import views

urlpatterns = [
    path(
        'home/',
        views.home,
        name='home',
    ),
    path(
        'detalhe/<int:id>',
        views.detalhe_livro,
        name='detalhe_livro',
    ),
    path(
        'cadastrar-livro/',
        views.cadastrar_livro,
        name='cadastrar_livro',
    ),
    path(
        'excluir-livro/<int:id>',
        views.excluir_livro,
        name='excluir_livro',
    ),
    path(
        'cadastrar-categoria/',
        views.cadastrar_categoria,
        name='cadastrar_categoria',
    ),
    path(
        'cadastrar-emprestimo',
        views.cadastrar_emprestimo,
        name='cadastrar_emprestimo',
    ),
    path(
        'devolver-livro/',
        views.devolver_livro,
        name='devolver_livro',
    ),
    path(
        'altualizar-livro/',
        views.atualizar_livro,
        name='atualizar_livro',
    ),
    path(
        'seus-emprestimos/',
        views.seus_emprestimos,
        name='seus_emprestimos',
    ),
    path(
        'processa_avaliacao/',
        views.processa_avaliacao,
        name="processa_avaliacao",
    ),
]
