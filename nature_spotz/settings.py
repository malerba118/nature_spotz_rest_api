"""
Django settings for nature_spotz project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import socket
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gd4jv&6e(ba(mrrr!2my!)4kr6_!i7%#a=xjctk!!oajg^7i+8'

# SECURITY WARNING: don't run with debug turned on in production!

PRODUCTION_SERVER = socket.gethostname() == "ip-172.31.19.202"



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_api',
    'django.contrib.gis',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nature_spotz.urls'

WSGI_APPLICATION = 'nature_spotz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if PRODUCTION_SERVER:

    DEBUG = False
    TEMPLATE_DEBUG = False

    ALLOWED_HOSTS = ["*",]

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'nature_spotz_db',
            'USER': 'malerba118',
            'PASSWORD': 'barbier118',
            'HOST': 'nature-spotz-db.c3spk20myn8l.us-west-2.rds.amazonaws.com',
            'PORT': '5432',
        }
    }

else:

    DEBUG = True
    TEMPLATE_DEBUG = True

    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'nsdb2',
            'USER': 'admin',
            'PASSWORD': 'admin',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',

    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_api.pagination.StandardResultsSetPagination',
}


if PRODUCTION_SERVER:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(os.path.join(BASE_DIR, 'static'), "static")
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR, 'static'), "media")

else:
    STATIC_URL = "/static/"
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(BASE_DIR, "static", "static-only")
    MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static", "static"),
    )