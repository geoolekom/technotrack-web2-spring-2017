from django.db.models import signals
from django.dispatch import receiver

from notifications.models import Notification
from feed.models import Post, FeedElement
from relations.models import Friendship


@receiver(signals.post_save, sender=Post)
def create_feed_element_on_post(instance, created=False, *args, **kwargs):
	if created:
		for friendship in instance.author.friends.all():
			FeedElement.objects.create(
				consumer_id=friendship.friend_id,
				target=instance
			)


@receiver(signals.post_save, sender=Notification)
def create_feed_element_on_notification(instance, created=False, *args, **kwargs):
	if created:
		FeedElement.objects.create(
			consumer_id=instance.consumer_id,
			target=instance
		)


@receiver(signals.post_delete, sender=Post)
@receiver(signals.post_delete, sender=Notification)
def delete_feed_element_on_delete(instance, *args, **kwargs):
	instance.feed_elements.all().delete()

