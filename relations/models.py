from django.db import models
from core.models import Authored
from django.conf import settings


class FriendshipRequest(models.Model, Authored):
	target = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Цель')
	accepted = models.BooleanField(verbose_name='Принят?')

	class Meta:
		verbose_name = 'Запрос в друзья'
		verbose_name_plural = 'Запросы в друзья'


class Friendship(models.Model):
	person = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Друг')

	class Meta:
		verbose_name = 'Запись о дружбе'
		verbose_name_plural = 'Записи о дружбе'
