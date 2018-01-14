# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0029_auto_20160117_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='source',
            field=models.TextField(max_length=40000, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='rate',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'new'), ('complete', 'complete'), ('canceledByCustomer', 'canceledByCustomer'), ('canceledByVendor', 'canceledByVendor')], default='new', max_length=20, null=True),
        ),
    ]
