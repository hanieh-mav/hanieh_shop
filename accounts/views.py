from django.forms.forms import Form
from django.shortcuts import render , redirect , get_object_or_404
from .forms import LoginUserForm , RegisterUserForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from django.contrib.auth import views as auth_view
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.

def loginUser(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,email = cd['email'],password = cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request, 'you logged in successfully', 'success')
                if user.is_admin or user.is_shopadmin :
                    return redirect('shop:home')
                else:
                    return redirect('shop:home')
            else:
                messages.error(request, 'ایمیل یا رمز عبور اشتباه میباشد', 'danger')    
    else:
        form = LoginUserForm()    
    return render(request,'accounts/login.html',{'form':form}) 


class UserPassReset(auth_view.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class PassWordResetDone(auth_view.PasswordResetDoneView):
    template_name = 'accounts/reset_done.html'


class PasswordResetConfirm(auth_view.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(auth_view.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


def RegisterUser(request):
    if request.method == "POST":
        form =RegisterUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(email=cd['email'],first_name=cd['first_name'],last_name=cd['last_name'],
            password=cd['password2'],phone=cd['phone'],ostan=cd['ostan'],zipcode=cd['zipcode'])
            user.save()
            messages.success(request, 'you registered successfully', 'success')
            return redirect('shop:home')
    else:
        form = RegisterUserForm()
    return render(request,'accounts/register.html',{'form':form})


