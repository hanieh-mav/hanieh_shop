# Generated by Django 3.2.4 on 2021-06-05 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام دسته بندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='ادرس دسته بندی')),
                ('is_subcat', models.BooleanField(default=False, verbose_name=' ایا سر دسته است ')),
                ('subcat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scat', to='shop.category', verbose_name='سردسته')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['name'],
            },
        ),
    ]