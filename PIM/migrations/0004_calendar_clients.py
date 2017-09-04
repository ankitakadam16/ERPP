# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-04 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientRelationships', '0011_auto_20170904_0752'),
        ('PIM', '0003_blogpost_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='clients',
            field=models.ManyToManyField(blank=True, related_name='calendarEntries', to='clientRelationships.Contact'),
        ),
    ]
