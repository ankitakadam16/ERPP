# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-08 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskBoard', '0005_auto_20160508_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='files',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='taskBoard.media'),
        ),
    ]
