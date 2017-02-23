from django.db import models
from core.models import Authored, Dated, Titled
from django.conf import settings


class Chat(Authored, Dated, Titled):
	participants = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Участники')

	class Meta:
		verbose_name = 'Чат'
		verbose_name_plural = 'Чаты'


class Message(Authored, Dated):
	chat = models.ForeignKey(Chat, verbose_name='Чат')
	content = models.TextField(verbose_name='Содержимое')

	class Meta:
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'
		get_latest_by = 'pub_time'

