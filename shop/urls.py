from django.urls import path
from .views import home , category_detail

app_name = 'shop'
urlpatterns = [
    path('',home,name='home'),
    path('page/<int:page>',home,name='home'),
    # path('detail/<int:pk>',detail,name='detail'),
    path('category/<slug:slug>',category_detail,name='category_detail'), 
    path('category/<slug:slug>/<int:page>',category_detail,name='category_detail'), 
  
    ]