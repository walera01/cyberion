from django import template
from ..forms import *
from ..models import *



register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('drugs/list_categories.html')
def show_categories():
    category = Category.objects.all()
    subcategories = SubCategory.objects.all()
    return {'category': category,
            'subcategories': subcategories}

@register.filter()
def formin():
    return Prise
