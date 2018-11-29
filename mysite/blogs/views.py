# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView


from .models import BlogAuthor, BlogComment, BlogPost

# Create your views here.


def index(request, username = None):
    first_name = ''
    last_name = ''
    if username:
        user = User.objects.get(username=username)
        post_list = BlogPost.objects.filter(user=user)

    else:
        post_list = BlogPost.objects.all()

    post_list = post_list.order_by('-pub_date')

    paginator = Paginator(post_list, 6)
    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts': posts, 'first_name': first_name, 'last_name': last_name})


class CreateComment(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['body']
    template_name = 'create_comment.html'
    login_url = reverse_lazy('login')

    def check_form(self, form):
        form.instance.user = self.request.user
        form.instance.post = BlogPost.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post', kwargs={'pk': self.kwargs['pk']})


class Registration(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'email']
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def check_form(self, form):
        form.instance.password = make_password(form.instance.password)
        return super().form_valid(form)


class Post(generic.DetailView):
    model = BlogPost
    template_name = 'post.html'

    def get_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = BlogComment.objects.filter(post=self.kwargs['pk'])
        context['comments'] = comments
        return context


class CreatePost(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'body']
    template_name = 'create_post.html'
    login_url = reverse_lazy('login')

    def check_form(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'body']
    template_name = 'create_post.html'
    login_url = reverse_lazy('login')

    def test(self):
        return Post.objects.get(id=self.kwargs['pk']).user == self.request.user


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')

    def test(self):
        return Post.objects.get(id=self.kwargs['pk']).user == self.request.user
