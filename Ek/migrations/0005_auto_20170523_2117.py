# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 21:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ek', '0004_auto_20170523_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecto',
            name='data',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='projecto',
            name='imagemDeCapa',
            field=models.ImageField(blank=True, upload_to='Projectos'),
        ),
    ]
