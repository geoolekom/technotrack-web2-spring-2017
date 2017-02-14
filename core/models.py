from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Authored(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        abstract = True
