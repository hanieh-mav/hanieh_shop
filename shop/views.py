from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product , Category
from comment.models import Comment
from django.core.paginator import Paginator
from django.views.generic import DetailView
from comment.forms import CommentForm
from cart.forms import CartAddForm
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from django.utils.decorators import method_decorator


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def home(request,page=1):
    products_list = Product.active.all()
    paginator = Paginator(products_list,8)
    products = paginator.get_page(page)
    return render(request,'shop/index.html',{'products':products,})




def category_detail(request,slug,page=1):
    category = get_object_or_404(Category,slug=slug)
    product = category.pcat.filter(is_active=True,status='p',storage__gt=0)
    paginator = Paginator(product,8)
    products = paginator.get_page(page)
    return render(request,'shop/index.html',{'products':products}) 


@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class ProductDetail(DetailView):
    def get_queryset(self,**kwargs):
        pk = self.kwargs.get('pk')
        return Product.active.filter(pk=pk)

    def get_context_data(self, **kwargs) :
        context = super(ProductDetail,self).get_context_data(**kwargs)
        product = Product.objects.get(pk=self.kwargs['pk'])
        related_products = Product.active.filter(category__in=product.category.all()).distinct()     
        related_products = related_products.exclude(id=product.id)[:4]
        comment = Comment.objects.filter(product=product)
        comment_form = CommentForm
        reply_form = CommentForm


        context.update({
            'related_products': related_products,
            'comment' : comment,
            'comment_form':comment_form,
            'reply_form':reply_form,
            'cart_form':CartAddForm

        })
        return context