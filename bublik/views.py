from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'bublik/product_list.html', {'products': products})

def order_new(request):
    if request.method == 'POST':
        products = {key: value for key, value in request.POST.items() if key.startswith('product_')}
        
        # Обработка данных формы

        return redirect('product_list')