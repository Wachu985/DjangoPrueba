
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'empleados',
        'USER':'postgres',
        'PASSWORD':'caperia985',
        'HOST':'127.0.0.1',
        'PORT':'5433',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR/'static/']

"""Configurando la URL con que van a salir los Archivos Media"""
MEDIA_URL = '/media/'
"""Configurando la direccion de la Carpeta Media"""
MEDIA_ROOT = BASE_DIR
