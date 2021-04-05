from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
# Create your views here.


def Contact(request):
    return HttpResponse('<h3>Contact Us</h3>')

def cartV(request):
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
        new_cart.save()
    
    if the_id:
        try:
            cartobj = Cart.objects.get(id=the_id)
            cartobj.save()
            context={'cart':cartobj}
        except:
            context={'empty':True}
        
    else:
        cart = None
        context={'empty':True}
    
    return render(request,'QR/cart.html',context)

def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        pass
    cartitem = CartItem.objects.get(id=id)
    cartitem.cart = None
    cartitem.save()
    return redirect('qr:cart')

def store(request,itemname='all'):

    if itemname=='all':
        products = Item.objects.all()
    else:
        products = Item.objects.filter(desc=itemname)
    context = {
                'products': products
            }

    return render(request, 'QR/store.html', context)


def addCartV(request,itemid):

    itemid = int(itemid)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    try:
        cartobj = Cart.objects.all().get(id=the_id)
    except:
        cartobj =Cart()
        cartobj.id = the_id
        cartobj.save()


    try:
        item = Item.objects.get(id = itemid)
    except:
        pass
    
    cart_item ,created = CartItem.objects.get_or_create(cart=cartobj,item=item,quantity=1,line_total=0)
    

    if created:
        new_total = 0
        for i in cartobj.cartitem_set.all():
            new_total = new_total + (i.item.price)
        cartobj.total = new_total
        request.session['items_count'] = cartobj.cartitem_set.count()
        cartobj.save()

    return redirect('qr:store','all')
