from django import template
from drugs.models import *
from drugs.forms import *


register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('drugs/list_categories.html')
def show_categories():
    category = Category.objects.all()
    return {'category': category}

@register.filter()
def formin():
    return Prise
