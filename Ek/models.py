# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ModelsLibraries import *
from Choices import *



class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    departamentos=models.CharField(max_length=100, blank=True)
    tutor = models.BooleanField(default=False)
    autor = models.BooleanField(default=False)
    editorial = models.CharField(blank=True, max_length=140)
    bio  = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='perfis',blank=True, max_length=100)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='r')

    class Meta:
        verbose_name_plural = 'Usuários do Site'
    def __str__(self):
        return self.nome
#end Pessoa
