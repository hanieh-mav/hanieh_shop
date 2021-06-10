from django.db import models

# Create your models here.


class Setting(models.Model):
    address = models.TextField(verbose_name='ادرس')
    phone = models.CharField(max_length=11,verbose_name='تلفن')
    email = models.EmailField(verbose_name='ایمیل')
    website = models.CharField(verbose_name='ادرس سایت',max_length=100)
    instagram = models.URLField(verbose_name='ادرس اینستاگرام',null=True,blank=True)
    twiiter  = models.URLField(verbose_name='ادرس توییتر',null=True,blank=True)


    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیمات'