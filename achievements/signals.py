from django.db.models import signals
from notifications.models import Notification
from achievements.models import Achievement


def check_if_unique(instance, created=False, *args, **kwargs):
	if instance.pk:
		return ValueError('Достижение уже было некогда получено!')


def notice_on_achievement(instance, created=False, *args, **kwargs):
	if created:
		Notification.objects.create(
			consumer_id=instance.author_id,
			content='Получено достижение {0}'.format(instance.title)
		)

signals.pre_save.connect(check_if_unique, sender=Achievement)
signals.post_save.connect(notice_on_achievement, sender=Achievement)
