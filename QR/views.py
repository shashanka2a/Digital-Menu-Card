from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
from cart.cart import Cart

# Create your views here.

present_pk=0

def Contact(request):
    return HttpResponse('<h3>Contact Us</h3>')

def store(request,pk):
    products = Item.objects.all()
    present_pk=pk
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

def cart_add(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("store",present_pk)


def item_clear(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

def item_increment(request, id):
    cart = Cart(request)
    product = Item.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

def item_decrement(request, id):
    cart = Cart(request)
    for pro in cart.session['cart'].values():
        quan = pro['quantity']
    if(quan==1):
        item_clear(request,id)

    product = Item.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

def cart_detail(request):
    cart = Cart(request)
    dic = list(cart.session['cart'].values())
    total_price = sum([each['quantity']*(float(each['price'])) for each in dic])
    context = {"total":total_price}

    return render(request, 'cart_detail.html',context)


def order(request):
    cart = Cart(request)
    table_obj = Table.objects.get_or_create(table_no=present_pk)
    dic = list(cart.session['cart'].values())
    total_price = sum([each['quantity'] * (float(each['price'])) for each in dic])
    for prod in cart.session['cart'].values():
        OrderItem.objects.create(table=table_obj[0],name=prod['name'],price=str(prod['price']),quantity=prod['quantity'])
    cart.clear()
    return redirect('store',present_pk)
