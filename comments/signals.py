from django.db.models import signals
from django.dispatch import receiver

from comments.models import Comment
from notifications.models import Notification
from achievements.models import Achievement, comments


@receiver(signals.post_save, sender=Comment)
def notice_and_achieve_on_comment(instance, created=False, *args, **kwargs):
	target = instance.target
	if hasattr(target, 'author_id') and created and target.author_id != instance.author_id:
		Notification.objects.create(
			consumer_id=target.author_id,
			content='{0} прокомментировал ваш {1} с id = {2}'.format(instance.author, target._meta.verbose_name, target.id)
		)

		num = target.comments.count()
		if num in comments.keys():
			Achievement.objects.update_or_create(
				author_id=target.author_id,
				title=comments[num],
				defaults={
					'content': 'У вас {0} комментов на {1} с id = {2}!'.format(num, str(target._meta.verbose_name), target.id)
				}
			)

signals.post_save.connect(notice_and_achieve_on_comment, sender=Comment)
