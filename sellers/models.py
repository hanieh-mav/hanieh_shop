from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save
from django.shortcuts import reverse
from shop.models import Product


# Create your models here.


class Seller(models.Model):
    products = models.ManyToManyField(Product,blank=True,related_name='product')
    user = OneToOneField(get_user_model(),verbose_name='کاربر',on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100,verbose_name='اسم شرکت')
    logo = models.ImageField(upload_to = 'logo/%Y/%M/%d', verbose_name='لوگو')
    email = models.EmailField(verbose_name='ایمیل شرکت')
    phone = models.CharField(verbose_name='تلفن شرکت',max_length=11)
    is_active = models.BooleanField(default=False,verbose_name='وضعیت')
  


    def __str__(self):
        return '{}-{}'.format(self.user,self.company_name)
 

    def get_absolute_url(self): 
        return reverse('dashboard:index')


    def product_to_str(self):
        return '-'.join([product.name for product in self.products.all()])


def save_seller(sender, **kwargs):
	if kwargs['created']:
		p1 = Seller(user=kwargs['instance'])
		p1.save()

post_save.connect(save_seller, sender=get_user_model())