from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name
