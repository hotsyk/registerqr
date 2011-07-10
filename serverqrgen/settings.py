import os
import sys

DIRNAME = os.path.dirname(__file__)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SERVE_STATIC_FILES = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True


STATICFILES_ROOT = os.path.join(DIRNAME, 'media')
STATIC_ROOT = ''
STATICFILES_DIRS = (
    os.path.join(DIRNAME, 'media'),
)
STATIC_DIRS = (
    os.path.join(DIRNAME, 'media'),
)
STATICFILES_URL = '/media/'
STATIC_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '-8qmss7rgj@ej^583&$4h97=k9fikjm6+i$r$70s2aw+9buw&-'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates'),
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'dynamicresponse.middleware.api.APIMiddleware',
    'dynamicresponse.middleware.dynamicformat.DynamicFormatMiddleware',
    )

ROOT_URLCONF = 'serverqrgen.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'serverqrgen.api',
    'serverqrgen.core',
    'serverqrgen.generator',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_FROM = '"ServerQRgenerator" <gotsyk@gmail.com>'

MAINTENANCE_MODE = False

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {  # optional
            'DB': 1,
            'PASSWORD': None,
        },
    },
}


SOUTH_TESTS_MIGRATE = False

try:
    import local_settings
    for param in dir(local_settings):
        if not '__' in param:
            setattr(sys.modules[__name__], param,\
                getattr(local_settings, param))
except ImportError:
    pass
