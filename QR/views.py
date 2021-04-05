from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
# Create your views here.


def Contact(request):
    return HttpResponse('<h3>Contact Us</h3>')


def store(request,itemname='all'):

    if itemname=='all':
        products = Item.objects.all()
    else:
        products = Item.objects.filter(desc=itemname)
    context = {
                'products': products
            }

    return render(request, 'QR/store.html', context)
