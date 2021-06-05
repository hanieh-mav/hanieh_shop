from django.urls import path
from .views import home 

app_name = 'shop'
urlpatterns = [
    path('',home,name='home'),
    path('page/<int:page>',home,name='home'),
    # path('detail/<int:pk>',detail,name='detail'),
  
    ]