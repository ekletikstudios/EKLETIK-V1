# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 22:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ek', '0006_projecto_informacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projecto',
            old_name='imagemDeCapa',
            new_name='capa',
        ),
    ]
