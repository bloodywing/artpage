from .base import *


DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


try:
    from .local import *
except ImportError:
    pass
