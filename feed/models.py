from django.db import models
from core.models import Authored, Dated, Titled, Deletable, Consumed, BoundAble
from comments.models import CommentAble
from likes.models import LikeAble


class Post(Authored, Dated, Titled, Deletable, LikeAble, CommentAble):
	content = models.TextField(verbose_name=u'Содержание')

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'


class FeedElement(Consumed, BoundAble, Dated):

	class Meta:
		verbose_name = 'Запись в ленте'
		verbose_name_plural = 'Записи в ленте'
