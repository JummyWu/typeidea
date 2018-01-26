# coding:utf-8

from .base import * # NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': 3306,
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


INSTALLED_APPS += [
    'debug_toolbar',
  #  'silk',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
   # 'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
SILKY_PYTHON_PROFILER = True
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL':'//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'
}

