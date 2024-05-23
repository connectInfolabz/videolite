# In myapp/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter("remove_spaces")
def remove_spaces(value):
    return value.replace(' ', '')
