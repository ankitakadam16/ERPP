# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0040_auto_20160214_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='heading',
            field=models.CharField(max_length=75, null=True),
        ),
    ]
