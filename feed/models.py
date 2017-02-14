from django.db import models
from core.models import Authored, Dated


class Post(models.Model, Authored, Dated):
	title = models.CharField(verbose_name='Заголовок', max_length=200)
	content = models.TextField(verbose_name=u'Текст поста')
	rating = models.IntegerField('Рейтинг', default=0)

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'



