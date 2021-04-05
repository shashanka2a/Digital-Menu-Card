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

    fried = Item.objects.filter(desc="Fried")
    noodles = Item.objects.filter(desc="Noodles")
    manchuria = Item.objects.filter(desc="Manchurian")
    cooldrinks = Item.objects.filter(desc="Cooldrink")
    biryani = Item.objects.filter(desc="Biryani")

    context = {'products': products,
               'fried': fried,
               'noodles': noodles,
               'manchuria': manchuria,
               'cooldrinks': cooldrinks,
               'biryani': biryani
               }

    return render(request, 'store.html', context)
