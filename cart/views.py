from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from shop.models import Product
from .forms import CartAddForm
from django.views.decorators.http import require_POST 
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def detail(request):
	cart = Cart(request)
	return render(request, 'cart/detail.html', {'cart':cart})



@login_required
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product,pk=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        if (quantity > product.storage or quantity == 0):
            messages.error(request, 'مقدار وارد شده از موجودی بیشتر است', 'danger')
            return redirect('shop:product_detaill', product.pk)
        else:
            cart.add(product=product, quantity=quantity)
            return redirect('cart:detail')



@login_required
def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(Product, id=product_id)
	cart.remove(product)
	return redirect('cart:detail')