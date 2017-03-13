from django.db.models import signals
from django.dispatch import receiver

from feed.models import Post, FeedElement, FeedRelated


@receiver(signals.post_save, sender=Post)
def create_feed_element_on_post(instance, created=False, *args, **kwargs):
	if created:
		for friendship in instance.author.friends.all():
			FeedElement.objects.create(
				consumer_id=friendship.friend_id,
				target=instance
			)


def delete_feed_element_on_delete(instance, *args, **kwargs):
	instance.feed_elements.all().delete()

for subclass in FeedRelated.__subclasses__():
	signals.post_delete.connect(delete_feed_element_on_delete, sender=subclass)

