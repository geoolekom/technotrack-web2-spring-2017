from django.db import models
from core.models import Authored, Dated


class Chat(Authored, Dated):
	class Meta:
		verbose_name = 'Чат'
		verbose_name_plural = 'Чаты'


class Message(Authored, Dated):
	chat = models.ForeignKey(Chat, verbose_name='Чат')
	content = models.TextField(verbose_name='Содержимое')

	class Meta:
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'

