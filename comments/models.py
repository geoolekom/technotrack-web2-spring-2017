from django.db import models
from core.models import Authored, Dated, BoundAble, Deletable
from likes.models import LikeAble


class Comment(Authored, Dated, BoundAble, Deletable, LikeAble):
	content = models.TextField(verbose_name='Содержание')

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'


class CommentAble(models.Model):
	comments = BoundAble.get_relation(Comment)

	class Meta:
		abstract = True
