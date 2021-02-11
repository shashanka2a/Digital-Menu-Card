from django.contrib import admin
from .models import Item,User,Cart,CartItem
# Register your models here.


admin.site.register(User)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)