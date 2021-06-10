from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('partials/category/category_navbar.html')
def category_navbar():
    return {
        'category': Category.objects.all()
     }
