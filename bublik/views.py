from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import OrderForm, OrderpositionForm
from django.db import connection

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'bublik/product_list.html', {'products': products})

def order_new(request):
    if request.method == 'POST':
        products = {key: value for key, value in request.POST.items() if key.startswith('product_')}
        payment_method = request.POST.get('payment_method')

        if len(products) > 0:
            order_form = OrderForm()
            order = order_form.save(commit=False)
            order.payment_type = payment_method
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
    
# Не лучший вариант, но оставил raw sql
def reports(request):
    # product_table
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                    P.name,
                    P.price,
                    sum(POS.count) as cnt,
                    sum(P.price * POS.count) as sum
                from bublik_order as O
                inner join bublik_orderposition as POS on POS.order_id = O.id
                inner join bublik_product as P on POS.product_id = P.id
            group by P.name, P.price
        """)
        rows = cursor.fetchall()

    product_table = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

    # cash_table
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                sum(POS.count * P.price) as main,
                sum(case when O.payment_type = 'cash' then POS.count * P.price else 0 end) as cash,
                sum(case when O.payment_type = 'card' then POS.count * P.price else 0 end) as card,
                sum(case when O.payment_type = 'perevod' then POS.count * P.price else 0 end) as perevod
            from bublik_order as O
            inner join bublik_orderposition as POS on POS.order_id = O.id
            inner join bublik_product as P on POS.product_id = P.id
        """)
        rows = cursor.fetchall()

    cash_table = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

    return render(request, 'bublik/reports.html', {'product_table': product_table, 'cash_table': cash_table})