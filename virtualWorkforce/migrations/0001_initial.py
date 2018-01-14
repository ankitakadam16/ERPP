# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 11:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import virtualWorkforce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='logParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('typ', models.CharField(choices=[('string', 'string'), ('int', 'int'), ('boolean', 'boolean')], default='string', max_length=15)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='virtualWorkforceProcess', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='processFileVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(null=True, upload_to=virtualWorkforce.models.getProcessUploadsPath)),
                ('name', models.CharField(max_length=100, null=True)),
                ('version', models.CharField(max_length=5)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtualWorkforce.process')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processFiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='processRunLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('stageName', models.CharField(max_length=100)),
                ('stageType', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
                ('processFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtualWorkforce.processFileVersion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processRunLog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='logparameter',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logParameters', to='virtualWorkforce.processRunLog'),
        ),
    ]
