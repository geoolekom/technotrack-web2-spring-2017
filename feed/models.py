from django.db import models
from core.models import Authored, Dated, Titled, Deletable


class Post(Authored, Dated, Titled, Deletable):
	content = models.TextField(verbose_name=u'Содержание')

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

