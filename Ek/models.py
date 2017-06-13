# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date
from Choices import *


# from Ek._Models import Album
# from Ek._Models import Artigo
# from Ek._Models import Livro
# from Ek._Models import Pessoa
# from Ek._Models import Projecto
# from Ek._Models import Solicitacao

# from ._Models.Album import Album
# from ._Models.Artigo import Artigo
# from ._Models.Livro import Livro
# from ._Models.Pessoa import Pessoa
# from ._Models.Projecto import Projecto
# from ._Models.Solicitacao import Solicitacao


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    departamentos=models.CharField(max_length=100, blank=True)
    tutor = models.BooleanField(default=False)
    autor = models.BooleanField(default=False)
    editorial = models.CharField(blank=True, max_length=140)
    Bio  = models.TextField(blank=True)
    perfil = models.ImageField(upload_to='perfis',blank=True, max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='r')

    class Meta:
        verbose_name_plural = 'Usuários do Site'
    def __str__(self):
        return self.nome
#end Pessoa