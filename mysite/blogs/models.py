# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=1500)
    date = models.DateTimeField('Publishing date', auto_now_add=True)

    def __str__(self):
        return '"{title}" by {username}'.format(title=self.title, username=self.author.username)


class BlogComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.TextField(max_length=1000)
    comment = models.ForeignKey(BlogPost, max_length=500, on_delete=models.CASCADE)
    date = models.DateTimeField('Publishing date', auto_now_add=True)

    def __str__(self):
        return '"{body}..." from {post_title} by {username}'.format(body=self.comment[:25], post_title=self.post.title,
                                                                    username=self.author.username)

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})


class BlogAuthor(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        return self.user.username
