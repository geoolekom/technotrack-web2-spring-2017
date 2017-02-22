from django.db import models
from core.models import Authored, Dated, BoundAble, Deletable


class Comment(Authored, Dated, BoundAble, Deletable):
	content = models.TextField(verbose_name='Содержание')

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
