from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post


# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'car_sales/home.html', context)


def about(request):
    return render(request, 'car_sales/about.html', {'title': 'About'})
