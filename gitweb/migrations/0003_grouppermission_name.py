# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-20 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitweb', '0002_auto_20160320_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouppermission',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
