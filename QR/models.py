from django.db import models

# Create your models here.

FOOD_CHOICES = [
    ('all', 'all'),
    ('biryani', 'biryani'),
    ('manchuria', 'manchuria'),
    ('friedRice','friedRice'),
    ('noodles','noodles'),
    ('cooldrinks','cooldrinks')
]

class Item(models.Model):
    name = models.CharField(max_length=30,null=False)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    desc = models.CharField(max_length=50,default="all")

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    table_id = models.CharField(max_length=20, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.table_id)


class OrderItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)