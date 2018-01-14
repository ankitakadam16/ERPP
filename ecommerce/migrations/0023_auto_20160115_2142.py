# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-15 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0022_auto_20160115_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='unit',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='genericproduct',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='generictype',
            name='icon',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='generictype',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
