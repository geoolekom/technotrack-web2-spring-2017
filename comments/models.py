from django.db import models

from core.models import Authored, Dated, BoundAble, Deletable
from core.decorators import non_editable_fields
from likes.models import LikeAble


@non_editable_fields('author_id', 'target_content_type_id', 'target_id')
class Comment(Authored, Dated, BoundAble, Deletable, LikeAble):
    content = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return 'Коммент {0} на {1} с id = {2}: {3}' \
            .format(self.author, self.target._meta.verbose_name, self.target.id, self.content)


class CommentAble(models.Model):
    comments = BoundAble.get_relation(Comment)

    class Meta:
        abstract = True
