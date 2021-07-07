from django.contrib import admin
from django.urls import path , include 
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls')),
    path('accounts/',include('accounts.urls')),
    path('comment/',include('comment.urls')),
    path('contact/',include('contactus.urls')),
    path('cart/',include('cart.urls')),
    path('orders/',include('orders.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('sellers/',include('sellers.urls')),
    path('debug/', include(debug_toolbar.urls)),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
