# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-24 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ek', '0010_artigo_who'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artigo',
            name='who',
        ),
    ]
