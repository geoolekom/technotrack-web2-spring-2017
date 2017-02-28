from django.db import models
from core.models import Authored, Dated, Titled, Deletable, Consumed, BoundAble
from comments.models import CommentAble
from likes.models import LikeAble


class FeedElement(Consumed, BoundAble, Dated):
	class Meta:
		verbose_name = 'Запись в ленте'
		verbose_name_plural = 'Записи в ленте'

	def __str__(self):
		return "Лента {0}: {1}".format(self.consumer, str(self.target))


class FeedRelated(models.Model):
	feed_elements = BoundAble.get_relation(FeedElement)

	class Meta:
		abstract = True


class Post(Authored, Dated, Titled, Deletable, LikeAble, CommentAble, FeedRelated):
	content = models.TextField(verbose_name=u'Содержание')

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

	def __str__(self):
		return 'пост "{0}: {1}"'.format(self.author.username, self.title)


