from django.urls import path
from .views import RegisterSeller ,ProfileUpdate,CreateSellerProduct

app_name = 'sellers'

urlpatterns = [
    path('register',RegisterSeller,name='register-seller'),
    path('profile/update/<int:pk>',ProfileUpdate.as_view(),name='profile-update'),
    path('create/seller/<int:pk>',CreateSellerProduct.as_view(),name='product_seller'),

    
]