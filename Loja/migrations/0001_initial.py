# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 07:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('artista', models.CharField(max_length=50)),
                ('gravadora', models.CharField(max_length=50)),
                ('capa', models.ImageField(default=0, upload_to=b'Loja/Albums')),
                ('faixas', models.IntegerField()),
                ('faixa_1', models.CharField(blank=True, max_length=50)),
                ('faixa_2', models.CharField(blank=True, max_length=50)),
                ('faixa_3', models.CharField(blank=True, max_length=50)),
                ('faixa_4', models.CharField(blank=True, max_length=50)),
                ('faixa_5', models.CharField(blank=True, max_length=50)),
                ('faixa_6', models.CharField(blank=True, max_length=50)),
                ('faixa_7', models.CharField(blank=True, max_length=50)),
                ('faixa_8', models.CharField(blank=True, max_length=50)),
                ('faixa_9', models.CharField(blank=True, max_length=50)),
                ('faixa_10', models.CharField(blank=True, max_length=50)),
                ('faixa_11', models.CharField(blank=True, max_length=50)),
                ('faixa_12', models.CharField(blank=True, max_length=50)),
                ('faixa_13', models.CharField(blank=True, max_length=50)),
                ('faixa_14', models.CharField(blank=True, max_length=50)),
                ('faixa_15', models.CharField(blank=True, max_length=50)),
                ('editorial', models.CharField(blank=True, max_length=500)),
                ('ficheiro', models.FileField(default=0, upload_to=b'Vendas', verbose_name=b'Ficheiro a baixar')),
                ('preco', models.FloatField(default=0, verbose_name=b'Pre\xc3\xa7o em d\xc3\xb3lares')),
                ('download', models.BooleanField(default=True, verbose_name=b'Pra baixar')),
                ('status', models.CharField(choices=[('d', 'Rascunho'), ('p', 'Publicado'), ('o', 'Oculto'), ('r', 'Em Revis\xe3o')], default=b'd', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('lancamento', models.DateField(default=datetime.date.today, verbose_name=b'Lan\xc3\xa7amento')),
                ('editora', models.CharField(max_length=50)),
                ('paginas', models.IntegerField(verbose_name=b'P\xc3\xa1ginas')),
                ('capa', models.ImageField(default=0, upload_to=b'Loja/Livros')),
                ('cap_1', models.CharField(blank=True, max_length=70)),
                ('cap_2', models.CharField(blank=True, max_length=70)),
                ('cap_3', models.CharField(blank=True, max_length=70)),
                ('cap_4', models.CharField(blank=True, max_length=70)),
                ('cap_5', models.CharField(blank=True, max_length=70)),
                ('cap_6', models.CharField(blank=True, max_length=70)),
                ('cap_7', models.CharField(blank=True, max_length=70)),
                ('cap_8', models.CharField(blank=True, max_length=70)),
                ('cap_9', models.CharField(blank=True, max_length=70)),
                ('cap_10', models.CharField(blank=True, max_length=70)),
                ('cap_11', models.CharField(blank=True, max_length=70)),
                ('cap_12', models.CharField(blank=True, max_length=70)),
                ('cap_13', models.CharField(blank=True, max_length=70)),
                ('cap_14', models.CharField(blank=True, max_length=70)),
                ('cap_15', models.CharField(blank=True, max_length=70)),
                ('editorial', models.CharField(blank=True, max_length=500)),
                ('ficheiro', models.FileField(default=0, upload_to=b'Vendas', verbose_name=b'Ficheiro a baixar')),
                ('preco', models.FloatField(default=0, verbose_name=b'Pre\xc3\xa7o em d\xc3\xb3lares')),
                ('download', models.BooleanField(default=True, verbose_name=b'Pra baixar')),
                ('status', models.CharField(choices=[('d', 'Rascunho'), ('p', 'Publicado'), ('o', 'Oculto'), ('r', 'Em Revis\xe3o')], default=b'r', max_length=1)),
            ],
        ),
    ]
