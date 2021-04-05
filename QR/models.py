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
