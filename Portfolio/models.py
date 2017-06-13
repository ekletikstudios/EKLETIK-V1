# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Ek.models import *
from datetime import date
from Choices import *



# Create your models here.
class Projecto(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    informacao = models.TextField(default="Etiam porta sem malesuada magna mollis euismod. Praesent commodo cursus magna...")
    detalhes_tecnicos = models.CharField(max_length=200, blank=True)

    totalCores = 0

    cor_1 = models.CharField(max_length=7, blank=True)
    cor_2 = models.CharField(max_length=7, blank=True)
    cor_3 = models.CharField(max_length=7, blank=True)
    cor_4 = models.CharField(max_length=7, blank=True)

    capa = models.ImageField(upload_to='projectos', blank=True)
    local = models.CharField(max_length=100)
    dias = models.IntegerField(default=1)

    destaque = models.BooleanField(default=False)
    data = models.DateField(auto_now=False, default=date.today)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='r')

    class Meta:
        verbose_name_plural = 'Portfolio'

    def __str__(self):
        return self.nome

    def Cores(self):
        return self.totalCores
#end Projecto