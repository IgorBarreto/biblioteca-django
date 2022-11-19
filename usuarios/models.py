from hashlib import sha256

from django.db import models


# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    senha = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.nome}'

    def save(self, *args, **kwargs):
        self.senha = sha256(self.senha.encode()).hexdigest()
        super(Usuario, self).save(*args, **kwargs)

    @classmethod
    def verificar_senha(cls, senha_salva, senha):
        print(sha256(senha.encode()).hexdigest())
        print(senha_salva)
        return sha256(senha.encode()).hexdigest() == senha_salva
