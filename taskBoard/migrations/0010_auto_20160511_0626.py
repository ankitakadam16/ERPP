# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 00:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskBoard', '0009_auto_20160511_0550'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='timelineitem',
            unique_together=set([('commit', 'task')]),
        ),
    ]
