from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Authored(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Автор',
        related_name='%(class)s_authored'
    )

    class Meta:
        abstract = True


class Consumed(models.Model):
    consumer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Потребитель'
    )

    class Meta:
        abstract = True


class Dated(models.Model):
    pub_time = models.DateTimeField(verbose_name='Время публикации', auto_now_add=True)
    upd_time = models.DateTimeField(verbose_name='Последнее изменение', auto_now=True)

    class Meta:
        abstract = True


class Titled(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Deletable(models.Model):
    deleted = models.BooleanField(verbose_name='Удален?', default=False)

    class Meta:
        abstract = True


class BoundAble(models.Model):
    target = GenericForeignKey('target_content_type', 'target_id')
    target_content_type = models.ForeignKey(ContentType)
    target_id = models.PositiveIntegerField()

    @staticmethod
    def get_relation(model):
        if issubclass(model, BoundAble):
            return GenericRelation(model, content_type_field='target_content_type', object_id_field='target_id')
        else:
            return None

    class Meta:
        abstract = True
