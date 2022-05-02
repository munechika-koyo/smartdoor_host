"""
Django settings for development
"""
import os
from .settings_common import *


SECRET_KEY = "django-insecure-&5b%$lzy8+@$n33)2i)_$04mqjn78ej$+9(2he6_g#mev6*h!6"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

# Logging setting
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "loggers": {
        # Django logger
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        # keymanagement logger
        "keymanagement": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        # authenticate_api logger
        "authenticate_api": {
            "handlers": ["console"],
            "level": "DEBUG",
        }
    },

    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "dev"
        },
    },

    "formatters": {
        "dev": {
            "format": "\t".join([
                "%(asctime)s",
                "[%(levelname)s]",
                "%(pathname)s(Line:%(lineno)d)",
                "%(message)s"
            ])
        },
    }
}
