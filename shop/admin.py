from django.contrib import admin
from .models import Product 


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','image_tag','storage','is_active')
    list_filter = ('price','created')
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name','description')
    actions = ['make_published']

    def make_published(self,request,queryset):
       row =  queryset.update(status='p')    
       self.message_user(request,f'{row} تغییر کرد به منشر شده')
    make_published.short_description = "تغییر وضییت انتشار به منشر شده"



# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name','slug','subcat','is_subcat')
#     list_filter = ('name','is_subcat')
#     prepopulated_fields = {'slug':('name',)}
#     search_fields = ('name',)




 