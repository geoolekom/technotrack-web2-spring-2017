from django.dispatch import receiver
from django.db.models import signals

from likes.models import Like
from notifications.models import Notification
from achievements.models import Achievement, likes


@receiver(signals.post_save, sender=Like)
def notice_and_achieve_on_like(instance, created=False, *args, **kwargs):
	target = instance.target
	if hasattr(target, 'author_id') and created and target.author_id != instance.author_id:

		Notification.objects.create(
			consumer_id=target.author_id,
			content='{0} поставил лайк на ваш {1} с id = {2}'.format(instance.author, target._meta.verbose_name, target.id)
		)

		num = target.likes.count()
		if num in likes.keys():
			Achievement.objects.update_or_create(
				author_id=target.author_id,
				title=likes[num],
				defaults={
					'content': 'У вас {0} лайков на {1} с id = {2}!'.format(num, target._meta.verbose_name, target.id)
				}
			)


@receiver(signals.post_delete, sender=Like)
def notice_on_like_delete(instance, *args, **kwargs):
	target = instance.target
	if hasattr(target, 'author_id') and target.author_id != instance.author_id:
		Notification.objects.create(
			consumer_id=target.author_id,
			content='{0} убрал лайк с вашего {1} с id = {2}'.format(instance.author, target._meta.verbose_name, target.id)
		)

