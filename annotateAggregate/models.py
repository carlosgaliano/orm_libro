from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    seller = models.ForeignKey(Seller, related_name="orders", on_delete=models.PROTECT)
    total = models.DecimalField(max_digits=18, decimal_places=9)

    def __str__(self):
        return self.seller.name
