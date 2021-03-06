# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 07:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PIM', '0003_blogpost_public'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='PIM.blogPost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogsBookmarked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
