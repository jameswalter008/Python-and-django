"""App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('customers/<int:id>',views.customers,name='customers.show'),
    path('product_page/',views.product,name='products'),
    path('',views.dashboard,name='dashboard'),
    path('order/create/<int:customerID>',views.ordercreate,name='order.create'),
    path('order/update/<int:orderID>',views.orderupdate,name='order.update'),
    path('order/delete/<int:orderID>',views.orderdelete,name='order.delete'),
]
