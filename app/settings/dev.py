from .base import *  # noqa

DEBUG = True

SECRET_KEY = "django-insecure-73p2%6_@-*l2cgtm#3p9l_wem^hf!mtgr3hmas&1pk_el_)c*e"

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
