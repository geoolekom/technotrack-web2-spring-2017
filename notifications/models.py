from django.db import models
from core.models import Dated, Deletable, Consumed


class Notification(Consumed, Dated, Deletable):
	content = models.TextField(verbose_name='Содержимое')

	class Meta:
		verbose_name = 'Уведомление'
		verbose_name_plural = 'Уведомления'
