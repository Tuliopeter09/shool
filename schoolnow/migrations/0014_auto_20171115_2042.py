# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-15 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolnow', '0013_auto_20171115_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensagem',
            name='memorando',
            field=models.TextField(max_length=400),
        ),
    ]
