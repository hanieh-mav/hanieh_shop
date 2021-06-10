from django.urls import path
from .views import add_comment , add_reply

app_name = 'comment'
urlpatterns = [
    path('add_comment/<int:product_pk>/', add_comment, name='add_comment'),
    path('add_reply/<slug:product_pk>/<int:comment_pk>',add_reply,name='add_reply'),
]