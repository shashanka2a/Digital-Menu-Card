from django.urls import path
from .views import Contact, store,Istore
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', store, name='index'),
    path('store/<str:pkk>',Istore,name='iiindex'),
    path('contact/', Contact, name='contact')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
