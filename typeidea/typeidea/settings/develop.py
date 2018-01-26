# coding:utf-8

from .base import * # NOQA


DEBUG = True

DATABASES = {
    'default':{
	'ENGINE':'django.db.backends.sqlite3',
	'NAME':os.path.join(BASE_DIR,'db.sqlite3'),
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
    #'silk',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'silk.middleware.SilkyMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']
SILKY_PYTHON_PROFILER = True
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL':'//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'brief': {
            'format':'%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'debug.log',
        },
        'console': {
            'level': 'DEBUG',
            'formatter': 'brief',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
