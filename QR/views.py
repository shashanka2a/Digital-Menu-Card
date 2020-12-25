from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
# Create your views here.


def home(request):
    return render(request, 'home.html')


def Contact(request):
    return HttpResponse('<h3>Contact Us</h3>')


def store(request):
    products = Item.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)
