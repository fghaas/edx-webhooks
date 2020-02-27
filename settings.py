"""
Django test settings for edx_shopify project.

Generated by 'django-admin startproject' using Django 1.8.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'foobar'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django_nose',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'djcelery',
    'edx_shopify',
]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

CELERY_ALWAYS_EAGER = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

ROOT_URLCONF = 'edx_shopify.urls'

SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = 'http://localhost:18000'
SOCIAL_AUTH_EDX_OAUTH2_KEY = 'key'
SOCIAL_AUTH_EDX_OAUTH2_SECRET = 'secret'

WEBHOOK_SETTINGS = {
    'edx_shopify': {
        'shop_domain': 'example.com',
        'api_key': 'foobar',
    }
}
