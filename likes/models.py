from django.db import models
from core.models import Authored, BoundAble


class Like(Authored, BoundAble):

	class Meta:
		verbose_name = 'Лайк'
		verbose_name_plural = 'Лайки'


class LikeAble(models.Model):
	likes = BoundAble.get_relation(Like)

	class Meta:
		abstract = True
