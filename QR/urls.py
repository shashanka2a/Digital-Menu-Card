from django.urls import path
from .views import home, Contact, store
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', home, name='home'),
    path('store', store, name='store'),
    path('contact/', Contact, name='contact')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
