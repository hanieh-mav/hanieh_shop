# Generated by Django 3.2.4 on 2021-06-10 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created'], 'verbose_name': 'نظر', 'verbose_name_plural': 'نظرات'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_reply',
            field=models.BooleanField(default=False, verbose_name='ایا یک پاسخ است؟'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pcomment', to='shop.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='romment', to='comment.comment', verbose_name='پاسخ'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ucomment', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
