from django.urls import path
from .views import  cart_add 

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_pk>' ,cart_add,name='cart_add'),
]