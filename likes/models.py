from django.db import models
from core.models import Authored, BoundAble


class Like(Authored, BoundAble):

	def save(self, *args, **kwargs):
		if Like.objects.filter(
			author_id=self.author_id,
			target=self.target
		):
			raise ValueError('Лайк этого автора уже стоит на этом объекте!')
		else:
			return super(Like, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Лайк'
		verbose_name_plural = 'Лайки'


class LikeAble(models.Model):
	likes = BoundAble.get_relation(Like)

	class Meta:
		abstract = True
