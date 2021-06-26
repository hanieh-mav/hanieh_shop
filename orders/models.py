from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from shop.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Order(models.Model):
    SEND_CHOICES = (
        ('p','on proccess'),
        ('s','sent'),
        ('o','out of Storage'),
        ('w','Waiting')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='uorder',verbose_name='کاربر')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False,verbose_name='وضعیت پرداخت')
    status = models.CharField(max_length=1,choices=SEND_CHOICES,default='w',verbose_name='وضعیت سفارش')
    discount = models.IntegerField(blank=True, null=True, default=None,verbose_name='تخفیف')

    class Meta:
        ordering = ['is_paid','status','-created']

    def __str__(self):
        return str(self.user)

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.item.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int( total - discount_price )
        return total

  
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='item',verbose_name='ایتم ها')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_item',verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت')
    quantity = models.PositiveSmallIntegerField(default=1,verbose_name='تعداد')

    def __str__(self):
        return str(self.pk)

    def get_cost(self):
        return self.price*self.quantity



class Coupon(models.Model):
	code = models.CharField(max_length=30, unique=True,verbose_name='کد')
	valid_from = models.DateTimeField(verbose_name='زمان شروع')
	valid_to = models.DateTimeField(verbose_name='زمان انقضا')
	discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],verbose_name='مقدار')
	active = models.BooleanField(default=False,verbose_name='وضعیت')




	def __str__(self):
		return self.code

    



