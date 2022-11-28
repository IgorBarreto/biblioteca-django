from django.contrib import admin

from .models import Categoria, Emprestimo, Livros

# Register your models here.
admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Emprestimo)
