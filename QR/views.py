from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
from cart.cart import Cart

# Create your views here.

present_pk=0

def store(request,pk):
    products = Item.objects.all()
    global present_pk
    present_pk = pk
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
               'biryani': biryani,
               'pk':pk,
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
    global present_pk
    cart = Cart(request)
    dic = list(cart.session['cart'].values())
    total_price = sum([each['quantity']*(float(each['price'])) for each in dic])
    context = {"total":total_price , "table_no" :present_pk }

    return render(request, 'cart_detail.html',context)


def order(request):
    global present_pk
    cart = Cart(request)
    table_obj = Table.objects.get_or_create(table_no=present_pk,total=0)
    dic = list(cart.session['cart'].values())
    total_price = sum([each['quantity'] * (float(each['price'])) for each in dic])
    for prod in cart.session['cart'].values():
        OrderItem.objects.create(table=table_obj[0],name=prod['name'],price=str(prod['price']),quantity=prod['quantity'])
    tab_obj = Table.objects.filter(table_no=present_pk)
    tab_obj.total = total_price
    cart.clear()
    total = total_price
    return redirect('store',present_pk)

def orders_display(request):
    d = {} 
    tables = [elem[0] for elem in list(Table.objects.all().values_list('table_no'))]
    #print(tables)
    for i in range(len(tables)):
        table_obj = Table.objects.get(table_no = tables[i])
        orders = OrderItem.objects.filter(table=table_obj)
        d[tables[i]] = list(orders.values())
    #print(d)
    context = {"d":d}
    return render(request, 'orders_display.html',context)

def order_status(request,pk):
    d = {}
    tables = [elem[0] for elem in list(Table.objects.all().values_list('table_no'))]
    if pk in tables:
        table_obj = Table.objects.get(table_no = pk)
        order = OrderItem.objects.filter(table=table_obj)
        d[pk] = list(order.values())
        context = {'d':d}
        return render(request, 'order_status.html',context)
    else:
        return HttpResponse('<br><br><br><h2><center>Order ready✔️</center></h2>')

def order_update(request,id):
    t = Table.objects.get(table_no = id)
    #o = OrderItem.objects.get(table=t)
    """    
    for ord in o:
        PreviousOrders.objects.create(table=id,name=ord.name,price=ord.price,quantity=ord.quantity)
    """
    t.delete()
    return redirect('orders_display')

