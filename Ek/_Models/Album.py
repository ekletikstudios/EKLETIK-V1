# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Choices import *


class Album(models.Model):
    tipo = 'Álbum'
    safeTipo = 'album'
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=50)
    gravadora = models.CharField(max_length=50)
    capa = models.ImageField(upload_to='Loja/Albums', max_length=100, default=0)
    faixas = models.IntegerField()
    faixa_1 = models.CharField(max_length=50, blank=True)
    faixa_2 = models.CharField(max_length=50, blank=True)
    faixa_3 = models.CharField(max_length=50, blank=True)
    faixa_4 = models.CharField(max_length=50, blank=True)
    faixa_5 = models.CharField(max_length=50, blank=True)
    faixa_6 = models.CharField(max_length=50, blank=True)
    faixa_7 = models.CharField(max_length=50, blank=True)
    faixa_8 = models.CharField(max_length=50, blank=True)
    faixa_9 = models.CharField(max_length=50, blank=True)
    faixa_10 = models.CharField(max_length=50, blank=True)
    faixa_11 = models.CharField(max_length=50, blank=True)
    faixa_12 = models.CharField(max_length=50, blank=True)
    faixa_13 = models.CharField(max_length=50, blank=True)
    faixa_14 = models.CharField(max_length=50, blank=True)
    faixa_15 = models.CharField(max_length=50, blank=True)

    editorial = models.CharField(max_length=500, blank=True)
    ficheiro = models.FileField(upload_to='Vendas', max_length=100, default=0, verbose_name='Ficheiro a baixar')
    preco = models.FloatField(default=0, verbose_name='Preço em dólares')
    download = models.BooleanField(default=True, verbose_name='Pra baixar')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='d')

    def __str__(self):
        return self.titulo
#end Album