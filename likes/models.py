from django.db import models
from core.models import Authored, BoundAble


#class LikeAble(models.Model):
	#likes = models.ForeignKey(Like, related_name='likes')


class Like(Authored, BoundAble):

	class Meta:
		verbose_name = 'Лайк'
		verbose_name_plural = 'Лайки'
