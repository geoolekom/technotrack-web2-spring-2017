from django.db.models import signals
from django.dispatch import receiver

from feed.models import FeedElement
from notifications.models import Notification


@receiver(signals.post_save, sender=Notification)
def create_feed_element_on_notification(instance, created=False, *args, **kwargs):
	if created:
		FeedElement.objects.create(
			consumer_id=instance.consumer_id,
			target=instance
		)
