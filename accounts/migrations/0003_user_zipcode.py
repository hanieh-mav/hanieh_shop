# Generated by Django 3.2.4 on 2021-06-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zipcode',
            field=models.IntegerField(blank=True, null=True, verbose_name='کدپستی'),
        ),
    ]
