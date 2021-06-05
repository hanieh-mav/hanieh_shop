from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import DetailView


# Create your views here.

def home(request,page=1):
    products_list = Product.objects.active()
    paginator = Paginator(products_list,8)
    products = paginator.get_page(page)
    return render(request,'shop/index.html',{'products':products,})