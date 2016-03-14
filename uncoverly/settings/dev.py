from .base import *

SECRET_KEY = "o-&zun-i6*umbzch#)pf4*+ao=bldb(!*fac^_640+#a5esti^"
DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

USE_LOCAL_DATABASE = True
if USE_LOCAL_DATABASE:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uncoverly',
        'USER': 'uncoverly',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
