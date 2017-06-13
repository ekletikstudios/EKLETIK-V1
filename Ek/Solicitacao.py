# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from Choices import *


class Solicitacao(models.Model):
    nomeDoCliente = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.IntegerField()
    website = models.URLField()
    tipoDoProjecto = models.CharField(max_length=1, choices=SOLICIT_CHOICES, default='w')
    descricaoDoProjecto = models.TextField()
    expectativaDeEntrega = models.DateField(default=date.today)
#end Solicitacao