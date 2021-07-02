from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Seller



@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user','company_name','product_to_str','is_active')
    list_filter = ('is_active',)
    search_fields = ('is_active',)
