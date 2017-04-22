from django.db import models

from core.models import Dated, Deletable, Consumed
from feed.models import FeedRelated


class Notification(Consumed, Dated, Deletable, FeedRelated):
    content = models.TextField(verbose_name='Содержимое')

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    def __str__(self):
        return 'уведомление "{0}: {1}"'.format(self.consumer.username, self.content)
