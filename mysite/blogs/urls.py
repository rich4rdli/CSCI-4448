from django.urls import path

from blogs.views import CreateComment, index, Post, CreatePost, EditPost, DeletePost

urlpatterns = [
    path('', index, name='index'),
    path('<str:username>', index, name='user_posts'),
    path('blog_post/<int:pk>/', Post.as_view(), name='post'),
    path('blog_post/create/', CreatePost.as_view(), name='create_post'),
    path('blog_post/create/<int:pk>/update', EditPost.as_view(), name='update_post'),
    path('blog_post/<int:pk>/delete/', DeletePost.as_view(), name='delete_post'),
    path('blog_post/<int:pk>/comment/', CreateComment.as_view(), name='create_comment')
    ]
