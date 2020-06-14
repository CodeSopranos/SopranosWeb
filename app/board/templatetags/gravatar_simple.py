from django.template import Library
from django.conf import settings

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import hashlib

register = Library()


@register.filter()
def gravatar_url(email=None, size=80):
    if email:
        url = 'http://www.gravatar.com/avatar/' + hashlib.md5(email.lower().encode('utf-8')).hexdigest() + '?'
        url += urlencode([
            ('s', str(size)),
            ('d', 'identicon')
        ])
    else:
        email_hash = ''
        url = 'http://www.gravatar.com/avatar/' + email_hash + '?'

        url += urlencode([
            ('s', str(size)),
            ('d', 'mp')
        ])
    return url
