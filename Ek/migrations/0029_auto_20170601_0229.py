# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ek', '0028_auto_20170601_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='teste',
        ),
        migrations.AddField(
            model_name='item',
            name='teste',
            field=models.ManyToManyField(default=1, to='Ek.AlbumItem'),
        ),
    ]
