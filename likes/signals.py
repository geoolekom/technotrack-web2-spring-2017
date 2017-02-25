from likes.models import Like
from django.db.models import signals
from notifications.models import Notification
from achievements.models import Achievement, likes


def check_if_unique(instance, *args, **kwargs):
	if instance.pk:
		raise ValueError('Переиспользование лайков в другом месте запрещено.')


def notice_and_achieve_on_like(instance, created=False, *args, **kwargs):
	target = instance.target
	if hasattr(target, 'author_id') and created and target.author_id != instance.author_id:
		consumer_id = target.author_id
		content = instance.author.username + ' поставил вам лайк на ' + \
			str(target._meta.verbose_name) + \
			' с id = ' + str(target.id)
		Notification.objects.create(consumer_id=consumer_id, content=content)

		num = target.likes.count()
		if num in likes.keys():
			Achievement.objects.create(
				author_id=target.author_id,
				title=likes[num],
				content='У вас {0} лайков на {1} с id = {2}!'.format(num, str(target._meta.verbose_name), target.id)
			)


def notice_on_like_delete(instance, *args, **kwargs):
	target = instance.target
	if hasattr(target, 'author_id') and target.author_id != instance.author_id:
		consumer_id = target.author_id
		content = instance.author.username + ' убрал лайк с ' + \
			str(target._meta.verbose_name) + \
			' с id = ' + str(target.id)
		Notification.objects.create(consumer_id=consumer_id, content=content)

signals.post_save.connect(notice_and_achieve_on_like, sender=Like)
signals.post_delete.connect(notice_on_like_delete, sender=Like)
signals.pre_save.connect(check_if_unique, sender=Like)
