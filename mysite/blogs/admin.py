# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import BlogAuthor, BlogComment, BlogPost

# Register your models here.

admin.site.register(BlogAuthor)
admin.site.register(BlogComment)
admin.site.register(BlogPost)



