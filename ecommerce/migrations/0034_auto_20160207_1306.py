# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 07:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0033_activebanner_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='activeBanner',
            new_name='offerBanner',
        ),
    ]
