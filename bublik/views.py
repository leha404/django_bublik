from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.filter()
    return render(request, 'bublik/product_list.html', {'products': products})