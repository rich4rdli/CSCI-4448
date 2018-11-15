# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Blogging website pre-alpha test!!!")


def postid(request, postid):
    return HttpResponse("Post ID of %s " % postid)


def content(request, postid):
    postcontent = "Content of post %s as follows: %s" % (postid, postid.postContent)
    return HttpResponse(postcontent)


def vote(request, postid):
    return HttpResponse("Voting on post %s" % postid)


def index(request):

    return render(request, 'blogs/index.html')