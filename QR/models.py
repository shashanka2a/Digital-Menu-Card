from django.db import models

# Create your models here.




class User(models.Model):
    tableId = models.CharField(max_length=30,null=False,blank=False)
    name = models.CharField(max_length=200,null=True,blank=True)
    phoneNo = models.CharField(max_length=20,null=True,blank=True)

    def __str__(self):
        return "Table No: "+ self.tableId + "Customer Name: "+self.name
        

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

