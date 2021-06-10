from django.urls import path
from .views import (loginUser ,UserPassReset ,
PassWordResetDone,
PasswordResetConfirm,
PasswordResetComplete,
RegisterUser)

app_name = 'accounts'

urlpatterns = [
    path('login/',loginUser,name='login'),
    path('register/',RegisterUser,name='register'),
    path('reset/', UserPassReset.as_view(), name='password_reset'),
    path('reset/done/', PassWordResetDone.as_view(), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/',PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('confirm/done/',PasswordResetComplete.as_view(), name='password_reset_complete'),
    
]