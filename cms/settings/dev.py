from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%$!zvb+l41kvobdsqo@_#(n%!7vtwy8fylbdqprtr3rdkls'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS.extend([
    'django_extensions',
])


try:
    from .local import *
except ImportError:
    pass
