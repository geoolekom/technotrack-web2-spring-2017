from django.db.models import signals
from notifications.models import Notification
from feed.models import Post, FeedElement
from relations.models import Friendship


def create_feed_element_on_post(instance, created=False, *args, **kwargs):
	if created:
		for friendship in Friendship.objects.filter(person=instance.author):
			FeedElement.objects.create(consumer_id=friendship.friend_id, target=instance)


def create_feed_element_on_notification(instance, created=False, *args, **kwargs):
	if created:
		FeedElement.objects.create(consumer_id=instance.consumer_id, target=instance)


signals.post_save.connect(create_feed_element_on_post, sender=Post)
signals.post_save.connect(create_feed_element_on_notification, sender=Notification)
