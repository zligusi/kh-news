from django.shortcuts import render
from .models import Artiles


def news(request):
    new = Artiles.objects.order_by('-data')
    return render(request , 'news/news.html', {'title':'News','new': new} )

def create (request):
    return render (request , 'news/create.html' , {'title' : 'create'})
