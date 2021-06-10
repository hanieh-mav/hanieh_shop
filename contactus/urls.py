from django.urls import path

from .views import ContactUs

app_name = 'contactus'
urlpatterns = [
    path('contact_us', ContactUs.as_view(), name='contact_us')
]