# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-21 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitweb', '0021_auto_20160521_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouppermission',
            name='limited',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='repopermission',
            name='limited',
            field=models.BooleanField(default=False),
        ),
    ]
