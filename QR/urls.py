from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('store/<int:pk>/', store, name='store'),
    path('contact/', Contact, name='contact'),
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',item_decrement, name='item_decrement'),
    path('cart/cart_clear/',cart_clear, name='cart_clear'),
    path('cart/cart-detail/',cart_detail,name='cart_detail'),
    path('orderAlP/',order,name='orderit')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
