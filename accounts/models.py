from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManger

# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=150, unique=True, verbose_name='آدرس ایمیل')
    phone = models.CharField(max_length=11, verbose_name='موبایل', null=True, blank=True)
    ostan = models.CharField(max_length=50, verbose_name='استان', null=True, blank=True)
    shahr = models.CharField(max_length=70, verbose_name='شهر', null=True, blank=True)
    address = models.TextField(verbose_name='آدرس', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    is_superuser = models.BooleanField(default=False, verbose_name='ادمین')
    is_shopadmin = models.BooleanField(default=False, verbose_name='مدیر فروشگاه')
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # this is for create super user in terminal
    REQUIRED_FIELDS = ['first_name', 'last_name','phone']

    objects = UserManger()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_lable):
        return True

    @property
    def is_staff(self):
        return self.is_admin            


 