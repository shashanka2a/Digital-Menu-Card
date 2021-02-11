from django.db import models

# Create your models here.

class User(models.Model):
    tableId = models.CharField(max_length=30,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    phoneNo = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return "Table No:   "+ self.tableId + "  Customer Name: "+self.name
        

DESC_CHOICES = [
    ('biryani','biryani'),
    ('cooldrinks','cooldrinks'),
    ('manchuria','manchuria'),
    ('noodles','noodles'),
    ('fried','fried')
]

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    desc = models.CharField(max_length=200,choices=DESC_CHOICES)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Cart(models.Model):
    total = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "Cart: " + str(self.id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True,blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    line_total = models.IntegerField(null=True,blank=True,default=0)


    def __str__(self):
        return "Cart: " + str(self.cart.id) + " CartItem:  " + str(self.id)

