# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-07 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20170707_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, null=True),
        ),
    ]
