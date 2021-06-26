from django.urls import path
from .views import detail , create , coupon_apply

app_name = 'orders'

urlpatterns = [
    path('<int:order_id>', detail ,name='detail'),
    path('create' , create ,name ='create'),
    path('apply/<int:order_id>/', coupon_apply, name='coupon_apply'),
]