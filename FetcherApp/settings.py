"""
Django settings for FetcherApp project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url
import secrets
import django_heroku


django_heroku.settings(locals())
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-0%@=&6(xxueyt8_zjl_wo*e))#+@0=dbt26a!8sffkq5%!9l@f'
# SECRET_KEY = os.environ.get("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = os.environ.get(
    "django-insecure-0%@=&6(xxueyt8_zjl_wo*e))#+@0=dbt26a!8sffkq5%!9l@f",
    default=secrets.token_urlsafe(nbytes=64),
)
IS_HEROKU_APP = "DYNO" in os.environ and not "CI" in os.environ
if not IS_HEROKU_APP:
    DEBUG = True
else: DEBUG = False
# DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
# ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
if IS_HEROKU_APP:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ['192.168.1.222', '.vercel.app','now.sh','127.0.0.1','localhost']

# Application definition

INSTALLED_APPS = [
    # 'whitenoise.runserver_nostatic'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Facebook',
    'fontawesomefree',
    'mathfilters',
    'django_user_agents'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    'ipinfo_django.middleware.IPinfoMiddleware',
]

IPINFO_TOKEN = '123456789abc'
IPINFO_SETTINGS = {
  'cache_options': {
      'ttl':30,
      'maxsize': 128
  }
}
IPINFO_FILTER = lambda request: request.scheme == 'http'
USER_AGENTS_CACHE = 'default'

ROOT_URLCONF = 'FetcherApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'FetcherApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASE_URL = 'postgres://u77400bp526m0m:pe41d200076f7b6be0e120a51eea721c6031cfc22fcb4711777ba20ef907f09d6@c1i13pt05ja4ag.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dbeppfmqrkpl86'
# DATABASE_URL = "postgresql://postgres:gAffjVocrJGjNPrvTVaLIDlVlKHUlknc@roundhouse.proxy.rlwy.net:34827/railway"

if IS_HEROKU_APP:
    # In production on Heroku the database configuration is derived from the `DATABASE_URL`
    # environment variable by the dj-database-url package. `DATABASE_URL` will be set
    # automatically by Heroku when a database addon is attached to your Heroku app. See:
    # https://devcenter.heroku.com/articles/provisioning-heroku-postgres#application-config-vars
    # https://github.com/jazzband/dj-database-url
    
    DATABASES = {
        "default": dj_database_url.config(
            env=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
            ssl_require=True,
        ),
    }
else:
    # When running locally in development or in CI, a sqlite database file will be used instead
    # to simplify initial setup. Longer term it's recommended to use Postgres locally too.
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STORAGES = {
    'default': 'django.core.files.storage.FileSystemStorage',
    # "staticfiles": {
    #     "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    # },
}
WHITENOISE_KEEP_ONLY_HASHED_FILES = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
