# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-21 10:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import finance.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ERP', '0008_auto_20161017_1748'),
        ('finance', '0010_auto_20170208_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ammount', models.PositiveIntegerField()),
                ('referenceID', models.CharField(max_length=30)),
                ('currency', models.CharField(choices=[('INR', 'INR'), ('USD', 'USD')], max_length=5)),
                ('dated', models.DateField()),
                ('attachment', models.FileField(null=True, upload_to=finance.models.getInflowAttachmentsPath)),
                ('description', models.TextField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('fromBank', models.CharField(max_length=30, null=True)),
                ('chequeNo', models.CharField(max_length=30, null=True)),
                ('mode', models.CharField(choices=[('cash', 'cash'), ('cheque', 'cheque'), ('wire', 'wire')], default='cash', max_length=20)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inflow', to='ERP.service')),
                ('toAcc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inflowCredits', to='finance.Account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inflowsTransacted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
