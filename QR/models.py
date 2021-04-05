from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField()

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Table(models.Model):
    table_no = models.IntegerField()

    def __int__(self):
        return self.table_no


class OrderItem(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=100,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
