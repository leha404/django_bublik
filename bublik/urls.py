from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('order/new/', views.order_new, name='order_new'),
    path('reports/', views.reports, name='reports'),
    path('orders/', views.order_list, name='order_list'),
]