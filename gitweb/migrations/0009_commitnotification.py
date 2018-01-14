# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-13 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gitweb', '0008_auto_20160414_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='commitNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sha', models.CharField(max_length=50)),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gitweb.repo')),
            ],
        ),
    ]
