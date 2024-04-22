from django.conf import settings
from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name + " - " + str(self.price)
class Order(models.Model):
    created_date = models.DateTimeField(default=timezone.localtime)
    # cash, card, perevod
    payment_type = models.CharField(max_length=10)
    products = models.ManyToManyField(Product, through="Orderposition")

    def __str__(self):
        return str(self.id) + " - " + str(self.created_date)
    
class Orderposition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return str("ord_" + str(self.order.id) + "_" + self.product.name)