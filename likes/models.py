from django.db import models
from django.core.exceptions import ValidationError

from core.models import Authored, Dated, BoundAble


class Like(Authored, Dated, BoundAble):

	def clean(self):
		if self.pk:
			raise ValidationError('Нельзя изменять существующие лайки!')
		return super(Like, self).clean()

	class Meta:
		verbose_name = 'Лайк'
		verbose_name_plural = 'Лайки'
		default_permissions = ('add', 'delete', )
		unique_together = (('author', 'target_content_type', 'target_id'),)


class LikeAble(models.Model):
	likes = BoundAble.get_relation(Like)

	class Meta:
		abstract = True
