# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-17 12:06
from __future__ import unicode_literals

import ERP.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ERP', '0006_device_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=300, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('pincode', models.PositiveIntegerField(null=True)),
                ('lat', models.CharField(max_length=15, null=True)),
                ('lon', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('link', models.TextField(max_length=300, null=True)),
                ('attachment', models.FileField(null=True, upload_to=ERP.models.getERPPictureUploadPath)),
                ('mediaType', models.CharField(choices=[('onlineVideo', 'onlineVideo'), ('video', 'video'), ('image', 'image'), ('onlineImage', 'onlineImage'), ('doc', 'doc')], default='image', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviceDocsUploaded', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('cin', models.CharField(max_length=100, null=True)),
                ('tin', models.CharField(max_length=100, null=True)),
                ('mobile', models.PositiveIntegerField()),
                ('telephone', models.CharField(max_length=20)),
                ('logo', models.CharField(max_length=200, null=True)),
                ('about', models.TextField(max_length=2000)),
                ('Doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='ERP.media')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERP.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicesCreated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]