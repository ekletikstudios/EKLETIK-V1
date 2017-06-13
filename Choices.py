# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date


STATUS_CHOICES = (
    ('d', 'Rascunho'),
    ('p', 'Publicado'),
    ('o', 'Oculto'),
    ('r', 'Em Revisão'),
)


PRODUCT_CHOICES = (
        ('a', 'Álbum'),
        ('i', 'Imagem'),
        ('v', 'Vídeo'),
        ('p', 'Livro'),
        ('m', 'Muse Template'),
        ('s', 'Sketch Template'),
        ('l', 'Ilustração'),
    )

SOLICIT_CHOICES = (
        ('a', 'Produção de Áudio'),
        ('i', 'Ilustração'),
        ('v', 'Produção e/ou Edição de Vídeo'),
        ('f', 'Fotografia'),
        ('w', 'Criação de Website'),
        ('d', 'Registrar Domínio'),
        ('l', 'Logotipo'),
    )

TOPIC_CHOICES  = ( ('N', 'Notícias'),
                       ('T', 'Tecnologia'),
                       ('A', 'Audio'),
                       ('V', 'Video'),
                       ('S', 'Ciência'),
                       ('P', 'Programação'),
                       ('G', 'Geral'),
                       ('C', 'Cultura'),
                       ('W', 'Web'),
                    )