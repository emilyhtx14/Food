from django import template
import math
register = template.Library()

@register.filter(name='divide')
def divide(value, arg):
    return math.trunc((value/arg) * 100)