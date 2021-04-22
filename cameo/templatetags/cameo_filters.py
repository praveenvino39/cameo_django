from django import template

register = template.Library()


@register.filter
def new_sale(value):
    return value + 1