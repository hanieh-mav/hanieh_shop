from django.urls import path
from .views import home , category_detail , ProductDetail

app_name = 'shop'
urlpatterns = [
    path('',home,name='home'),
    path('page/<int:page>',home,name='home'),
    path('category/<slug:slug>',category_detail,name='category_detail'), 
    path('category/<slug:slug>/<int:page>',category_detail,name='category_detail'), 
    path('detail/<int:pk>',ProductDetail.as_view(),name='product_detaill'), 
  
    ]