from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import CICharField


class Key(models.Model):
    """Registered NFC keys model
    """

    name = models.CharField(verbose_name="name", max_length=100)
    device = models.CharField(verbose_name="device", max_length=100)
    idm = CICharField(verbose_name="idm", max_length=16, unique=True)
    allow_423 = models.BooleanField(verbose_name="allow 423", null=True)
    allow_475 = models.BooleanField(verbose_name="allow 475", null=True)
    created_at = models.DateTimeField(verbose_name="creation time", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Key model"


class LoginUser(AbstractUser):
    """LoginUser model to access keymanagement app
    """

    class Meta:
        verbose_name_plural = "Login User"
