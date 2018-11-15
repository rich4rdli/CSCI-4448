from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:postId>/', views.postid(), name='postid'),

    path('<int:postId>/content/', views.content(), name='content'),

    path('<int:postId>/vote/', views.vote(), name='vote'),

]