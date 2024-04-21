from django import forms

from .models import Order, Orderposition

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('payment_type',)

class OrderpositionForm(forms.ModelForm):
    class Meta:
        model = Orderposition
        fields = ('count',)