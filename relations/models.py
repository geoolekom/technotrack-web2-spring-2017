from django.db import models
from django.conf import settings

from core.models import Authored, Dated
from core.decorators import non_editable_fields


@non_editable_fields('author_id', 'target_id')
class FriendshipRequest(Authored, Dated):
    target = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Цель')
    accepted = models.BooleanField(verbose_name='Принят?', default=False)

    class Meta:
        verbose_name = 'Запрос в друзья'
        verbose_name_plural = 'Запросы в друзья'
        unique_together = (('author', 'target'),)

    def __str__(self):
        return '{0} хочет подружиться с {1}'.format(self.author, self.target)


@non_editable_fields('person_id', 'friend_id')
class Friendship(models.Model):
    person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Пользователь',
        related_name='friends'
    )
    friend = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Друг',
        related_name='+'
    )

    class Meta:
        verbose_name = 'Запись о дружбе'
        verbose_name_plural = 'Записи о дружбе'
        unique_together = (('person', 'friend'),)
        default_permissions = ('add', 'delete',)

    def __str__(self):
        return '{0} дружит с {1}'.format(self.person, self.friend)
