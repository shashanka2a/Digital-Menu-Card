from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import *
# Create your views here.


def Contact(request):
    return HttpResponse('<h3>Contact Us</h3>')

def cartV(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None

    if the_id:
        new_total = 0
        line_total=0
        for i in cart.cartitem_set.all():
            line_total +=  float(i.item.price)*i.quantity
            new_total += line_total
        
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total=new_total
        cart.save()
        context={'cart':cart}
    else:
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
    
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cartobj = Cart.objects.get_or_create(id=the_id)
    cartinstance = Cart.objects.get(id=the_id)
    itemobj = Item.objects.get(id = itemid)
    cartitemobj =CartItem()
    cartitemobj.cart = cartinstance
    cartitemobj.item = itemobj
    cartitemobj.quantity=1
    cartitemobj.line_total = itemobj.price
    cartitemobj.save()

    return redirect('qr:store','all')


