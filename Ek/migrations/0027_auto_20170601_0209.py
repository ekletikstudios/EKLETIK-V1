# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ek', '0026_auto_20170601_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projecto',
            old_name='gestor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='projecto',
            old_name='titulo',
            new_name='nome',
        ),
        migrations.AddField(
            model_name='projecto',
            name='detalhes_tecnicos',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
