from datetime import date

from django.db import models
from django.utils import timezone

from usuarios.models import Usuario

# TODO ARRUMAR CONFIG ARQUIVOS ESSTATICOS

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.nome}'


class Livros(models.Model):
    img = models.ImageField(upload_to='capa_livro', null=True, blank=True)
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(
        max_length=30,
        blank=True,
    )
    data_cadastro = models.DateField(default=date.today)
    emprestado = models.BooleanField(default=False)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.DO_NOTHING,
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    class Meta:
        # verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return f'{self.nome}'


class Emprestimo(models.Model):
    choice_avaliacao = (
        ('P', 'Pésssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo'),
    )
    nome_emprestado = models.ForeignKey(
        Usuario, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    nome_emprestado_anonimo = models.CharField(
        max_length=30, blank=True, null=True
    )
    data_emprestimo = models.DateField(
        default=timezone.now,
    )
    data_devolucao = models.DateField(blank=True, null=True)
    livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    avaliacao = models.CharField(
        max_length=1, null=True, blank=True, choices=choice_avaliacao
    )

    def __str__(self):
        return f"{self.nome_emprestado} | {self.livro}"
