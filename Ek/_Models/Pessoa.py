# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Choices import *


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