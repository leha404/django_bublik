from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import OrderForm, OrderpositionForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'bublik/product_list.html', {'products': products})

def order_new(request):
    if request.method == 'POST':
        products = {key: value for key, value in request.POST.items() if key.startswith('product_')}
        
        order_form = OrderForm()
        order = order_form.save(commit=False)
        # TODO
        order.payment_type = 'cash'
        order.save()

        for p_key in products:
            product_id = p_key[8:]  # Извлекаем ID продукта, начиная с 9-го символа ключа
            product_quantity = products[p_key]  # Получаем количество продукта
            
            order_pos_form = OrderpositionForm()
            pos = order_pos_form.save(commit=False)
            
            product = get_object_or_404(Product, pk=product_id)
            
            pos.product = product
            pos.count = product_quantity
            pos.order = order
            
            pos.save()

        return redirect('product_list')