# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-22 03:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_timelineitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(related_name='projectsInvolvedIn', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectsInitiated', to=settings.AUTH_USER_MODEL),
        ),
    ]
