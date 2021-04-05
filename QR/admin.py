from django.contrib import admin
from .models import Item, OrderItem, Order
# Register your models here.
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
