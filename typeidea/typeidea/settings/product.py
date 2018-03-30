# coding:utf-8

from .base import * # NOQA
from decouple import config

DEBUG = config('DEBUG', default=True, cast=bool)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        # 'OPTIONS': {'charset': 'utf8mb4'}
    },
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PARSER_CLASS": "redis.connection.HiredisParser",
        }
    }
}


INSTALLED_APPS += [# NOQA
    'debug_toolbar',
  #  'silk',
]

MIDDLEWARE += [# NOQA
    'debug_toolbar.middleware.DebugToolbarMiddleware',
   #  'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
SILKY_PYTHON_PROFILER = True
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'
}
