# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Choices import *


class Livro(models.Model):
    tipo = 'Livro'
    safeTipo = 'livro'
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    lancamento = models.DateField(auto_now=False, default=date.today, verbose_name='Lançamento')
    editora = models.CharField(max_length=50)
    paginas = models.IntegerField(verbose_name='Páginas')
    capa = models.ImageField(upload_to='Loja/Livros', max_length=100, default=0)

    cap_1 = models.CharField(max_length=70, blank=True)
    cap_2 = models.CharField(max_length=70, blank=True)
    cap_3 = models.CharField(max_length=70, blank=True)
    cap_4 = models.CharField(max_length=70, blank=True)
    cap_5 = models.CharField(max_length=70, blank=True)
    cap_6 = models.CharField(max_length=70, blank=True)
    cap_7 = models.CharField(max_length=70, blank=True)
    cap_8 = models.CharField(max_length=70, blank=True)
    cap_9 = models.CharField(max_length=70, blank=True)
    cap_10 = models.CharField(max_length=70, blank=True)
    cap_11 = models.CharField(max_length=70, blank=True)
    cap_12 = models.CharField(max_length=70, blank=True)
    cap_13 = models.CharField(max_length=70, blank=True)
    cap_14 = models.CharField(max_length=70, blank=True)
    cap_15 = models.CharField(max_length=70, blank=True)

    editorial = models.CharField(max_length=500, blank=True)
    ficheiro = models.FileField(upload_to='Vendas', max_length=100, default=0, verbose_name='Ficheiro a baixar')
    preco = models.FloatField(default=0, verbose_name='Preço em dólares')
    download = models.BooleanField(default=True, verbose_name='Pra baixar')
    status = models.CharField(default='r', choices=STATUS_CHOICES, max_length=1)
    def __str__(self):
        return self.titulo
#end Livro