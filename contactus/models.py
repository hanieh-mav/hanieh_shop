from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=100,verbose_name='موضوع')
    body = models.TextField(verbose_name='متن')

    class Meta:
        verbose_name = 'ارتباط با ما'

    def __str__(self):
        return '{}-{}'.format(self.subject,self.name)


