from django.db import models
from accounts.models import User
from shop.models import Product
from django.shortcuts import reverse


# Create your models here.
class CommentManger(models.Manager):
    def reply(self):
        return self.filter(is_reply=True)




class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='ucomment',verbose_name='کاربر')
    body = models.TextField(verbose_name='متن')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,related_name='pcomment',verbose_name='محصول')
    reply = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='romment',verbose_name='پاسخ')
    is_reply = models.BooleanField(default=False,verbose_name='ایا یک پاسخ است؟')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return '{}-{}'.format(self.user,self.body)


    objects = CommentManger()

    def get_absolute_url(self):
        return reverse('shop:home')