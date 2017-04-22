from django.db import models

from core.models import Authored, Dated, BoundAble
from core.decorators import non_editable_fields


@non_editable_fields('author_id', 'target_content_type_id', 'target_id')
class Like(Authored, Dated, BoundAble):
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        default_permissions = ('add', 'delete',)
        unique_together = (('author', 'target_content_type', 'target_id'),)

    def __str__(self):
        return '{0} нравится {1} с id = {2}'.format(self.author, self.target._meta.verbose_name, self.target.id)


class LikeAble(models.Model):
    likes = BoundAble.get_relation(Like)

    class Meta:
        abstract = True
