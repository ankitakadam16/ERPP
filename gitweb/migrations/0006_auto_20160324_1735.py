# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-24 12:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gitweb', '0005_auto_20160322_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sshKey', models.CharField(max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devices', models.ManyToManyField(to='gitweb.device')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gitProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='repo',
            name='groups',
            field=models.ManyToManyField(to='gitweb.groupPermission'),
        ),
        migrations.AlterField(
            model_name='repo',
            name='perms',
            field=models.ManyToManyField(to='gitweb.repoPermission'),
        ),
    ]
