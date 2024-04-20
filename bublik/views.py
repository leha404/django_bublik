from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    
    # Разбиваем список продуктов на части по 2 элемента
    products_chunks = [products[i:i + 2] for i in range(0, len(products), 2)]
    
    return render(request, 'bublik/product_list.html', {'products_chunks': products_chunks})