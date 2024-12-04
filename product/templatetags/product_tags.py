from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('product/templatetags/menu.html')
def get_categories():
    categories = Category.objects.filter(parent__isnull=True)
    return {
        "categories":categories,
    }