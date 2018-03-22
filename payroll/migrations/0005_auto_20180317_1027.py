# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-17 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0004_auto_20180317_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='amount',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payslip',
            name='reimbursement',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payslip',
            name='total',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payslip',
            name='totalPayable',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
