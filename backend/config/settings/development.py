from .base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*.local']

INTERNAL_IPS = ['127.0.0.1']

if 'default' in DATABASES:
    DATABASES['default']['CONN_MAX_AGE'] = 0

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
