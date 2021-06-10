from django.shortcuts import redirect , get_object_or_404 
from .models import Comment
from django.contrib.auth.decorators import login_required
from shop.models import Product
from .forms import CommentForm
from django.contrib import messages

# Create your views here.


@login_required
def add_comment(request, product_pk):
    product = get_object_or_404(Product, id=product_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            newcomment = form.save(commit=False)
            newcomment.user = request.user
            newcomment.product = product
            newcomment.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد', 'success')

    return redirect('shop:product_detaill', product.id)


@login_required
def add_reply(request,product_pk,comment_pk):
    product = get_object_or_404(Product,pk=product_pk)
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            newreply = form.save(commit=False)
            newreply.user = request.user
            newreply.product = product
            newreply.reply = comment
            newreply.is_reply = True
            newreply.save()
            messages.success(request, 'پاسخ شما با موفقیت ثبت شد', 'success')

    return redirect('shop:product_detaill',product_pk)
