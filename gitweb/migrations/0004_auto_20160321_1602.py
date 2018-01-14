# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-21 10:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gitweb', '0003_grouppermission_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='gitGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('description', models.TextField(max_length=500)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='grouppermission',
            name='name',
        ),
        migrations.RemoveField(
            model_name='grouppermission',
            name='users',
        ),
        migrations.AddField(
            model_name='grouppermission',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gitweb.gitGroup'),
        ),
    ]
