# Generated by Django 3.2.4 on 2021-06-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='ادرس اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twiiter',
            field=models.URLField(blank=True, null=True, verbose_name='ادرس توییتر'),
        ),
    ]
