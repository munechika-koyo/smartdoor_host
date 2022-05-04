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
PATH_TO_LOGFILE = os.path.join(BASE_DIR, "logs", "django.log")
# if log file does not exist, generate 
if not os.path.exists(PATH_TO_LOGFILE):
    with open(PATH_TO_LOGFILE, "w") as f:
        f.write("")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "loggers": {
        # Django logger
        "django": {
            "handlers": ["file"],
            "level": "INFO",
        },
        # keymanagement logger
        "keymanagement": {
            "handlers": ["file"],
            "level": "INFO",
        },
        # authenticate_api logger
        "authenticate_api": {
            "handlers": ["file"],
            "level": "INFO",
        }
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": PATH_TO_LOGFILE,
            "formatter": "prod",
            "when": "D",  # log rotation (D=Day)
            "interval": 1,  # rotation frequency
            "backupCount": 7,  # saved number of files
        },
    },
    "formatters": {
        "prod": {
            "format": "\t".join(
                [
                    "%(asctime)s",
                    "[%(levelname)s]",
                    "%(message)s"
                ]
            )
        },
    },
}
