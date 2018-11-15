# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    userId = models.IntegerField(max_length=12, primary_key=True)
    userName = models.CharField(max_length=24)
    password = models.CharField(max_length=32)
    stars = models.IntegerField(default=0)

    def __str__(self):
        return self.userId


class Admin(User):
    adminId = models.IntegerField(max_length=12, primary_key=True)

    def __str__(self):
        return self.adminId


class Posts(models.Model):
    postId = models.IntegerField(max_length=12, primary_key=True)
    postDescription = models.TextField()
    postContent = models.TextField()

    def __str__(self):
        return self.postContent


