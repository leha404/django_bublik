from django.contrib import admin
from .models import Product, Order, Orderposition

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderposition)