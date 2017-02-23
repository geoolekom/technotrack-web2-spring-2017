from django.db import models
from core.models import Authored, Dated, Titled, Deletable
from comments.models import CommentAble
from likes.models import LikeAble


class Post(Authored, Dated, Titled, Deletable, LikeAble, CommentAble):
	content = models.TextField(verbose_name=u'Содержание')

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

