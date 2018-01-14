# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-25 06:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import finance.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ERP', '0008_auto_20161017_1748'),
        ('projects', '0006_auto_20160522_0311'),
        ('finance', '0003_auto_20161125_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('approvalMatrix', models.PositiveSmallIntegerField(default=1)),
                ('approvalStage', models.PositiveSmallIntegerField(default=0)),
                ('dispensed', models.BooleanField(default=False)),
                ('notes', models.TextField(max_length=500, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('settled', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.Transaction')),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenseSheet', to='finance.Transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenseGeneratedOrSubmitted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('currency', models.CharField(choices=[('INR', 'INR'), ('USD', 'USD')], max_length=5)),
                ('dated', models.DateTimeField()),
                ('attachment', models.FileField(null=True, upload_to=finance.models.getInvoicesPath)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERP.service')),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='finance.ExpenseSheet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceGeneratedOrSubmitted', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
