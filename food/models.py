from django.db import models


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10000, decimal_places=0)
    image = models.ImageField(upload_to='images/product')

    def __str__(self):
        return self.title
