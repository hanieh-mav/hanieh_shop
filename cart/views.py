from django.shortcuts import render, get_object_or_404 , redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from shop.models import Product
import redis
from django.conf import settings
from .forms import CartAddForm
from django.contrib import messages


# Create your views here.

redis_con = redis.Redis(settings.REDIS_HOST, settings.REDIS_PORT, settings.REDIS_DB)

@login_required
def cart_add(request,product_pk):
    product = get_object_or_404(Product,pk=product_pk)
    user = request.user
    print()

    if request.method == 'POST':
        form = CartAddForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if ( quantity > product.storage or quantity ==0 ):
                messages.success(request, 'مقدار وارد شده از موجودی بیشتر است', 'danger')
                return redirect('shop:product_detaill', product.pk)
            else:
                pass
    return redirect('shop:product_detaill', product.id)
