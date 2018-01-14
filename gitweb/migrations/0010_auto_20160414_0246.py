# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-13 21:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gitweb', '0009_commitnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='commitnotification',
            name='branch',
            field=models.CharField(default='master', max_length=100),
        ),
        migrations.AddField(
            model_name='commitnotification',
            name='message',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='commitnotification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
