from django.urls import path
from .views import RegisterSeller ,ProfileUpdate

app_name = 'sellers'

urlpatterns = [
    path('register',RegisterSeller,name='register-seller'),
    path('profile/update/<int:pk>',ProfileUpdate.as_view(),name='profile-update')
    
]