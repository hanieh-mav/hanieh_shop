from django.contrib.auth.models import User
from django.urls import path
from .views import (UserProfileUpdate, loginUser ,UserPassReset ,
PassWordResetDone,
PasswordResetConfirm,
PasswordResetComplete,
RegisterUser,
LogoutUser,
UserView,
UpdateView,
OrderDetail)

app_name = 'accounts'

urlpatterns = [
    path('login/',loginUser,name='login'),
    path('logout/',LogoutUser,name='logout'),
    path('register/',RegisterUser,name='register'),
    path('reset/', UserPassReset.as_view(), name='password_reset'),
    path('reset/done/', PassWordResetDone.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/',PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('confirm/done/',PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('user-detail/',UserView.as_view(),name='user_detail'),
    path('user-order/<int:pk>',OrderDetail.as_view(),name='order_detail'),
    path('user-update/<int:pk>',UserProfileUpdate.as_view(),name='user-update')
]