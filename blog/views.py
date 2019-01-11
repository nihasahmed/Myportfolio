from django.shortcuts import render
from .models import Post
# Create your views here.

def blogposts(request):

    content = Post.objects.all()
    return render(request,'blog/blog.html',{'content':content})
