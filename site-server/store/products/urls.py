
from django.contrib import admin
from django.urls import path
from products.views import add, basket_add

app_name = 'products'



urlpatterns = [
  path('', add, name='add'),
  path('basket/add/<int:product_id>/', basket_add, name='basket_add')
]
