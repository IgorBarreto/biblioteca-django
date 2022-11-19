# Generated by Django 4.1.3 on 2022-11-18 21:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Livros",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("autor", models.CharField(max_length=30)),
                ("co_autor", models.CharField(blank=True, max_length=30)),
                ("data_cadastro", models.DateField(default=datetime.date.today)),
                ("emprestado", models.BooleanField(default=False)),
                ("nome_emprestado", models.CharField(blank=True, max_length=30)),
                ("data_emprestimo", models.DateTimeField(blank=True)),
                ("data_devolucao", models.DateTimeField(blank=True)),
                ("tempo_duracao", models.DateField(blank=True)),
            ],
            options={
                "verbose_name_plural": "Livros",
            },
        ),
    ]
