from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    
    path('order/new/', views.order_new, name='order_new'),
    path('order/delete/', views.delete_order, name='delete_order'),
    path('orders/', views.order_list, name='order_list'),
    
    path('reports/', views.reports, name='reports'),
]