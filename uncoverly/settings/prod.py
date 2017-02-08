from .base import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = False

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

ALLOWED_HOSTS = ['*']
