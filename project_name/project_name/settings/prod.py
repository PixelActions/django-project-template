# settings/local.py
from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['.{{project_name}}.com','.pixelactions.com']
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('Kyriakos Toumbas', 'kyriakos@pixelactions.com'),
    ('Valentinos Evripidou', 'valentinos@pixelactions.com'),
)
SITE_URL = "http://{{project_name}}.com"
MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'username_{{project_name}}',
        'USER': 'username_{{project_name}}',
        'PASSWORD': '',
        'HOST': '',# Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',# Set to empty string for default.
    }
}

STATIC_ROOT = '/home/username/webapps/{{project_name}}_static/'
MEDIA_ROOT = '/home/username/webapps/{{project_name}}_media/'

'''
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = 
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[{{project_name}}] '
'''

'''
#Uncomment to use memcached. Configuration is the one provided on webfaction
#http://docs.webfaction.com/software/memcached.html

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/username/memcached.sock',
    }
}
'''
