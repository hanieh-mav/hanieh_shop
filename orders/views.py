from django.shortcuts import render , get_object_or_404 ,redirect
from .models import OrderItem , Order , Coupon
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .forms import CouponForm
from django.views.decorators.http import require_POST


# Create your views here.

@login_required
def detail(request,order_id):
	order = get_object_or_404(Order,id=order_id)
	form = CouponForm()
	return render(request, 'order/detail.html', {'order':order, 'form':form})



@login_required
def create(request):
    cart = Cart(request)
    user = request.user
    order = Order.objects.create(user=user)
    for item in cart:
        OrderItem.objects.create(order=order,product=item['product'],price=item['price'],
        quantity=item['quantity'])
        cart.clear()
        
    return redirect('orders:detail',order.id)



@require_POST
def coupon_apply(request, order_id):
	now = timezone.now()
	form = CouponForm(request.POST)
	if form.is_valid():
		code = form.cleaned_data['code']
		try:
			coupon = Coupon.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
			order = Order.objects.get(id=order_id)
			order.discount = coupon.discount
			order.save()
			return redirect('orders:detail', order_id)
		except Coupon.DoesNotExist:
			messages.error(request, 'این کد تخفیف وجود ندارد یا اشتباه است', 'danger')
			return redirect('orders:detail', order_id)