"""
Django settings for deploying
"""
import os
from .settings_common import *

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(",")

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    },
}

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        # Django logger
        "django": {"handlers": ["file"], "level": "INFO",},
        # keymanagement logger
        "keymanagement": {"handlers": ["file"], "level": "INFO",},
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(BASE_DIR, "logs/django.log"),
            "formatter": "prod",
            "when": "D",  # log rotation (D=Day)
            "interval": 1,  # rotation frequency
            "backupCount": 7,  # saved number of files
        },
    },
    "formatters": {
        "prod": {
            "format": "\t".join(["%(asctime)s", "[%(levelname)s]", "%(pathname)s(Line:%(lineno)d)", "%(message)s"])
        },
    },
}
