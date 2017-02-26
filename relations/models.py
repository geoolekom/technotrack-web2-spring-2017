from django.db import models

from core.models import Authored
from django.conf import settings


class FriendshipRequest(Authored):

	target = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Цель')
	accepted = models.BooleanField(verbose_name='Принят?', default=False)

	class Meta:
		verbose_name = 'Запрос в друзья'
		verbose_name_plural = 'Запросы в друзья'
		unique_together = (('author', 'target'), )


class Friendship(models.Model):
	person = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		verbose_name='Пользователь',
		related_name='+'
	)
	friend = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		verbose_name='Друг',
		related_name='friends'
	)

	class Meta:
		verbose_name = 'Запись о дружбе'
		verbose_name_plural = 'Записи о дружбе'
		unique_together = (('person', 'friend'), )
		default_permissions = ('add', 'delete', )
