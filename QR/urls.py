from django.urls import path
from .views import Contact, store
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', store, name='store'),
    path('<str:itemname>/', store, name='store'),
    path('contact/', Contact, name='contact')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
