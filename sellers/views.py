from shop.models import Product
from django.shortcuts import render , redirect , get_object_or_404 
from django.http import Http404
from django.contrib import messages
from accounts.forms import RegisterUserForm
from accounts.models import User
from django.contrib.auth import login
from .models import Seller
from django.views.generic import UpdateView , ListView
from .forms import CreateProductForm
from orders.models import Order


# Create your views here.


def RegisterSeller(request):
    if request.method == "POST":
        form =RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(email=cd['email'],first_name=cd['first_name'],last_name=cd['last_name'],
            password=cd['password2'],phone=cd['phone'],ostan=cd['ostan'],zipcode=cd['zipcode'])
            user.is_seller=True
            user.save()
            messages.success(request, 'شما ثبت نام شدید وارد شوید و اطلاعات خود را وارد کنید', 'success')
            login(request,user)
            return redirect('dashboard:profile-update',user.pk)
    else:
        form = RegisterUserForm()
    return render(request,'accounts/register.html',{'form':form})


class ProfileUpdate(UpdateView):
    model = Seller
    template_name = 'dashboard/profile_update.html'
    fields = ('company_name','logo','email','phone')

    def get_object(self):
        user = get_object_or_404(User,pk=self.kwargs['pk'])
        seller = Seller.objects.get(user=user)
        return seller



class CreateSellerProduct(UpdateView):
    model = Seller
    template_name = 'dashboard/seller_product.html'
    form_class = CreateProductForm

    def get_object(self):
        user = get_object_or_404(User,pk=self.kwargs['pk'])
        seller = Seller.objects.get(user=user)
        return seller



