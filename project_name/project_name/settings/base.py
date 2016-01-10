from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS, TEMPLATE_LOADERS, STATICFILES_FINDERS
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.join(BASE_DIR, '..')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{{secret_key}}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #For enable sitemaps
    #'django.contrib.sites',
    #'django.contrib.sitemaps',
    #For hooking up a robots.txt
    #'robots',
    #'crispy_forms',
    #'easy_thumbnails',
    #'rosetta',
	#'compressor',
	#'django_extensions',
	#'apps.pages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{{project_name}}.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
				'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'assets'),
)

WSGI_APPLICATION = '{{project_name}}.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')


#FOR MULTILINGUAL WEBSITES:
#   ENABLE THE LocalMiddelware EXACTLY after SessionMiddleware
#   Setup the project languages
'''

#ADD LocalMiddleware before Common but after session (sessions keeps/sets the selectred language so needs to come before)
MIDDLEWARE_CLASSES = (
	...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
)
#Specify required languages. IMPORTANT!:IF FORGOTTEN, Django will pick up ALL LANGUAGES!
LANGUAGES = (
    ('en', _('English')),
    ('el', _('Greek')),
)

#You can enable the i18n context processor and use the provided view to change between languages (or use different links with en/el values before the rest of the link
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
)
#Lastly, point to the LOCALE folder in your project, that the translations should be stored.
#Run ./manage.py makemessage -l <language code> 
#for each language, to generate the language file. later, with compilemessages, you can install the translations you used.
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
)
'''

'''
#FOR COMPRESSOR
STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)
'''

#GRAPPELI SETTINGS
#GRAPPELLI_ADMIN_TITLE = "{{project_name}} Administration"

#CRISPY FORMS SETTINGS
#CRISPY_TEMPLATE_PACK = 'bootstrap3'

'''
#EASY_THUMBNAILS SETTINGS
SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}
THUMBNAIL_SUBDIR = 'thumbs'
THUMBNAIL_ALIASES = {
    '': {
        'example': {'size': (400,0), 'crop':'scale'},
        'example2': {'size': (400,0), 'upscale': True, 'crop':'smart'},
    },
}
'''