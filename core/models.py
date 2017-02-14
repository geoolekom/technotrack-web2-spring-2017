from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Authored(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор')

	class Meta:
		abstract = True


class Dated(models.Model):
	pub_time = models.DateTimeField(verbose_name='Время публикации', auto_now_add=True)
	upd_time = models.DateTimeField(verbose_name='Последнее изменение', auto_now=True)

	class Meta:
		abstract = True


class User(AbstractUser, Dated):
	pass
