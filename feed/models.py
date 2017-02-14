from django.db import models
from core.models import Authored


class Post(models.Model, Authored):
	title = models.CharField(verbose_name='Заголовок', max_length=200)
	content = models.TextField(verbose_name=u'Текст поста')
	rating = models.IntegerField('Рейтинг', default=0)

	pub_time = models.DateTimeField('Время публикации', auto_now_add=True)
	upd_time = models.DateTimeField('Последнее изменение', auto_now=True)


