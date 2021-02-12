from django.urls import path
from .views import Contact, store,addCartV,cartV,remove_from_cart,UpdateItem
from django.conf import settings
from django.conf.urls.static import static


app_name = "qr"

urlpatterns = [
    path('store/<str:itemname>/', store, name='store'),
    path('additem/<int:itemid>/',addCartV,name='additemtocart'),
    path('contact/', Contact, name='contact'),
    path('cart/',cartV,name='cart'),
    path('updateitem/<int:id>',UpdateItem,name='updateitem'),
    path('remove/<int:id>',remove_from_cart,name='removefromcart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
