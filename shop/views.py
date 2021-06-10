from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product , Category
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic import DetailView


# Create your views here.

def home(request,page=1):
    products_list = Product.active.all()
    paginator = Paginator(products_list,8)
    products = paginator.get_page(page)
    return render(request,'shop/index.html',{'products':products,})


def category_detail(request,slug,page=1):
    category = get_object_or_404(Category,slug=slug)
    product = category.pcat.active()
    paginator = Paginator(product,8)
    products = paginator.get_page(page)
    return render(request,'shop/index.html',{'products':products}) 


class ProductDetail(DetailView):
    def get_queryset(self,**kwargs):
        pk = self.kwargs.get('pk')
        return Product.active.filter(pk=pk)

    def get_context_data(self, **kwargs) :
        context = super(ProductDetail,self).get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        related_products = Product.active.filter(category__in=product.category.all()).distinct()     
        related_products = related_products.exclude(id=product.id)[:4]


        context.update({
            'related_products': related_products,

        })
        return context