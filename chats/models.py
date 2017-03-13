from django.db import models
from core.models import Authored, Dated, Titled
from django.conf import settings


class Chat(Authored, Dated, Titled):
	participants = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name='Участники', blank=True)

	class Meta:
		verbose_name = 'Чат'
		verbose_name_plural = 'Чаты'

	def __str__(self):
		return self.title


class Message(Authored, Dated):
	chat = models.ForeignKey(Chat, verbose_name='Чат')
	content = models.TextField(verbose_name='Содержимое')

	class Meta:
		verbose_name = 'Сообщение'
		verbose_name_plural = 'Сообщения'
		get_latest_by = 'pub_time'

	def __str__(self):
		return '{0}, {1}: {2}'.format(self.chat_id, self.author, self.content)

