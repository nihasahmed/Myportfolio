from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.blogposts, name='blog' ),
    path('posts/<ids>', views.postsee, name='posts' ),




]
