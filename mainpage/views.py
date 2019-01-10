from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Works

# Create your views here.


def homepage(request):

    content = Works.objects.all()
    paginator = Paginator(content, 6)
    page = request.GET.get('page')
    contents =paginator.get_page(page)
    return render(request, 'mainpage/home.html', {'content': contents})

def details(request, ids):

    content = Works.objects.get(pk = ids)
    return render(request, 'mainpage/details.html', {'content': content})



def shop(request):

    content = Works.objects.all()
    return render(request, 'mainpage/shop.html', {'content': content})
