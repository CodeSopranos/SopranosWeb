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

@register.filter
def sort_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda kv: kv[1]))

@register.filter
def get_hashtags(text):
    hashtags = [word[1:] for word in text.split() if word[0] == '#']
    return set(hashtags)