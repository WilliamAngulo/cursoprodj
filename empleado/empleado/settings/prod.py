from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': BASE_DIR / 'db.sqlite3',
        #'NAME': BASE_DIR.child('db.sqlite3'), # este cambio permite saltar invonvenientes entre unipath y sqite3
        'NAME': 'dbempleado', # este fue el nombre que dimos en el postgresql shell
        'USER': 'williamangulo',
        'PASSWORD' : 'todopoderoso',
        'HOST' : 'localhost',
        'PORT' : '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')] # le decimos a Dango donde estan nuestros archivos estaticos

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
