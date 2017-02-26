from django.db.models import signals
from django.dispatch import receiver

from notifications.models import Notification
from achievements.models import Achievement


@receiver(signals.post_save, sender=Achievement)
def notice_on_achievement(instance, created=False, *args, **kwargs):
	if created:
		Notification.objects.create(
			consumer_id=instance.author_id,
			content='Получено достижение "{0}"'.format(instance.title)
		)

