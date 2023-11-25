from .base import *  # noqa

DEBUG = False

SECRET_KEY = "django-insecure-73p2%6_@-*l2cgtm#3p9l_wem^hf!mtgr3hmas&1pk_el_)c*e"

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://176.117.76.184:80",
    "http://176.117.76.184:433",
    "http://176.117.76.184",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
