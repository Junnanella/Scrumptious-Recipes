from django import template

register = template.Library()

register.filter


def resize_to(value):
    return value
