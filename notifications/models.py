from django.db import models
from core.models import Dated, Deletable
from django.conf import settings


class Notification(Dated, Deletable):
	content = models.TextField(verbose_name='Содержимое')
	receiver = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Получатель')

	class Meta:
		verbose_name = 'Уведомление'
		verbose_name_plural = 'Уведомления'
