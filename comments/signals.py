from django.db.models import signals
from comments.models import Comment
from notifications.models import Notification
from achievements.models import Achievement, comments


def notice_and_achieve_on_comment(instance, created=False, *args, **kwargs):
	target = instance.target
	if hasattr(target, 'author_id') and created and target.author_id != instance.author_id:
		consumer_id = target.author_id
		content = instance.author.username + ' прокомментировал ' + \
			str(target._meta.verbose_name) + \
			' с id = ' + str(target.id)
		note = Notification.objects.create(consumer_id=consumer_id, content=content)

		num = target.comments.count()
		if num in comments.keys():
			Achievement.objects.create(
				author_id=target.author_id,
				title=comments[num],
				content='У вас {0} комментов на {1} с id = {2}!'.format(num, str(target._meta.verbose_name), target.id)
			)

signals.post_save.connect(notice_and_achieve_on_comment, sender=Comment)
