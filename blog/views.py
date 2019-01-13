from django.shortcuts import render
from .models import Post
# Create your views here.

def blogposts(request):

    content = Post.objects.all()
    return render(request,'blog/blog.html',{'content':content})


def postsee(request, ids):
    content = Post.objects.get(pk = ids)
    return render(request, 'blog/post.html', {'content': content})
