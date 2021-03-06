# settings/local.py
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'username_{{project_name}}',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',# Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',# Set to empty string for default.
    }
}


'''
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = 
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[{{project_name}}] '
'''