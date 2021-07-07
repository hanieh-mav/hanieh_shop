from django.shortcuts import render , redirect , get_object_or_404
from .forms import LoginUserForm , RegisterUserForm , ChangeDetailuserForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import User
from django.contrib.auth import views as auth_view
from django.views.generic import UpdateView , DetailView
from django.views import View
from django.urls import reverse_lazy 
from orders.models import Order , OrderItem

# Create your views here.

def loginUser(request):

    """In This View Login with email and password and as role redirect to there page """

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,email = cd['email'],password = cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request, 'you logged in successfully', 'success')
                if user.is_admin or user.is_shopadmin or user.is_seller :
                    return redirect('dashboard:index')
                else:
                    return redirect('shop:home')
            else:
                messages.error(request, 'ایمیل یا رمز عبور اشتباه میباشد', 'danger')    
    else:
        form = LoginUserForm()    
    return render(request,'accounts/login.html',{'form':form}) 


class UserPassReset(auth_view.PasswordResetView):

    """In This View User enter email and get changr password email """

    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'


class PassWordResetDone(auth_view.PasswordResetDoneView):

    """In This View we send user to this page to say email sent"""

    template_name = 'accounts/reset_done.html'


class PasswordResetConfirm(auth_view.PasswordResetConfirmView):

    """In This View when user clicl on email link sen user to change pass"""

    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(auth_view.PasswordResetCompleteView):

    """In This View tell user changing is success or not """

    template_name = 'accounts/password_reset_complete.html'


def RegisterUser(request):

    """In This View register user """

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


def LogoutUser(request):
    logout(request)
    return redirect('shop:home')


@method_decorator(login_required, name='dispatch')
class UserView(View):
    template_name = 'accounts/user_view.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        user_detail = User.objects.get(id=user.id)
        orders = Order.objects.filter(user=user).order_by('-created')
        return render(request,self.template_name,{'orders':orders,'user':user_detail})



@method_decorator(login_required, name='dispatch')
class OrderDetail(DetailView):
    model = Order
    template_name = 'accounts/orderitem_detail.html'

 



@method_decorator(login_required, name='dispatch')
class UserProfileUpdate(UpdateView):
    model = User
    form_class = ChangeDetailuserForm
    success_url=reverse_lazy('accounts:user_detail')



