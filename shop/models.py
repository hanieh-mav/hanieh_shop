from django.db import models
from django.utils.html import format_html


# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته بندی')
    slug = models.SlugField(max_length=100,unique=True, verbose_name='ادرس دسته بندی')
    subcat = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='scat',verbose_name='سردسته')
    is_subcat = models.BooleanField(default=False,verbose_name=' ایا سر دسته است ')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']  
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'





class ProductManager(models.Manager):
    def active(self):
        return self.filter(is_active=True,status='p',storage__gt=0)


class Product(models.Model):
    STATUS_CHOICES = (
        ('d','پیش نویس'),
        ('p','منتشر شده')
    )
    name = models.CharField(max_length=100 , verbose_name='نام محصول')
    slug = models.SlugField(max_length=100,unique=True, verbose_name='ادرس محصول')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='pcat')
    photo = models.ImageField(upload_to = 'product/%Y/%M/%d', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')
    storage = models.IntegerField(verbose_name='موجودی')
    price = models.PositiveBigIntegerField(verbose_name='قیمت',default=0.0)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='d', verbose_name=' وضعیت انتشار')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['status','-created'] 


    def __str__(self):
        return self.name


    def image_tag(self):
        return format_html("<img src='{}' width =60 height=50>".format(self.photo.url))
    image_tag.short_description = 'تصویر'    



    def category_to_str(self):
        return '-'.join([category.name for category in self.category.all()])


    @property
    def is_availble(self):
        if self.storage == 0:
            return False
        else:
            return True
        
    objects = ProductManager()


