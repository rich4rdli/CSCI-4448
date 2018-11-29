# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .models import BlogAuthor, BlogComment, BlogPost

# Create your views here.


def index(request):
    return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})