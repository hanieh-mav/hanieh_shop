from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product , Category
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import DetailView


# Create your views here.

def home(request,page=1):
    products_list = Product.objects.active()
    paginator = Paginator(products_list,8)
    products = paginator.get_page(page)
    return render(request,'shop/index.html',{'products':products,})


def category_detail(request,slug,page=1):
    category = get_object_or_404(Category,slug=slug)
    product = category.pcat.active()
    paginator = Paginator(product,8)
    products = paginator.get_page(page)
    return render(request,'shop/index.html',{'products':products}) 