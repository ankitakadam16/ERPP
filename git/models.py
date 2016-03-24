from __future__ import unicode_literals
from django.contrib.auth.models import *
from django.db import models

# Create your models here.

class repoPermission(models.Model):
    user = models.ForeignKey(User , null = False)
    canRead = models.BooleanField(default = False)
    canWrite = models.BooleanField(default = False)
    canDelete = models.BooleanField(default = False)

class gitGroup(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length = 30 , null = True)
    description = models.TextField(max_length=500, null = False)

class groupPermission(models.Model):
    group = models.ForeignKey(gitGroup , null = True)
    canRead = models.BooleanField(default = False)
    canWrite = models.BooleanField(default = False)
    canDelete = models.BooleanField(default = False)

class device(models.Model):
    sshKey = models.CharField(max_length = 500 , null = True)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 50)

class profile(models.Model):
    user = models.ForeignKey(User , null =False , related_name='gitProfile')
    devices = models.ManyToManyField(device)


class repo(models.Model):
    perms = models.ManyToManyField(repoPermission )
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length = 30)
    creator = models.ForeignKey(User , null = False)
    groups = models.ManyToManyField(groupPermission )
    description = models.TextField(max_length=500, null = False)