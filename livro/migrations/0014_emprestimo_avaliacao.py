# Generated by Django 4.1.3 on 2022-11-21 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livro", "0013_alter_categoria_descricao"),
    ]

    operations = [
        migrations.AddField(
            model_name="emprestimo",
            name="avaliacao",
            field=models.CharField(
                choices=[
                    ("P", "Pésssimo"),
                    ("R", "Ruim"),
                    ("B", "Bom"),
                    ("O", "Ótimo"),
                ],
                default=1,
                max_length=1,
            ),
            preserve_default=False,
        ),
    ]
