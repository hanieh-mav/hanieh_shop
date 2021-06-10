from django import template
from ..models import Category
from setting.models import Setting

register = template.Library()

@register.inclusion_tag('partials/category/category_navbar.html')
def category_navbar():
    return {
        'category': Category.objects.all()
     }


@register.inclusion_tag('partials/base/footer_setting.html')
def shop_setting():
    return {
        'setting': Setting.objects.last()
     }
