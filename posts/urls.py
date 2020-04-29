# posts urls
from django.urls import path

from posts import views

irlpatterns = [
    path('/', views.list_posts, name='feed'),
    path('posts/new/', views.create_post, name='create_post'),
]