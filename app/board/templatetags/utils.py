from django.template import Library
from django.conf import settings

import hashlib

register = Library()

@register.filter
def get_keys(dictionary):
    return list(dictionary.keys())

@register.filter
def get_values(dictionary):
    return [dictionary[k] for k in dictionary]
