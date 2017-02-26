from django.db.models import signals, Q
from django.dispatch import receiver

from notifications.models import Notification
from achievements.models import Achievement, friendship
from relations.models import FriendshipRequest, Friendship


@receiver(signals.post_save, sender=FriendshipRequest)
def add_friendship_if_accepted(instance, created=False, *args, **kwargs):
	if instance.accepted:
		Friendship.objects.create(person=instance.author, friend=instance.target)
		Friendship.objects.create(person=instance.target, friend=instance.author)


@receiver(signals.post_save, sender=FriendshipRequest)
def note_on_friendship_request(instance, created=False, *args, **kwargs):
	if created:
		Notification.objects.create(
			consumer=instance.target,
			content='{0} хочет с вами подружиться'.format(instance.author.username)
		)


@receiver(signals.post_save, sender=Friendship)
def achieve_on_friendship(instance, created=False, *args, **kwargs):
	num = Friendship.objects.filter(person=instance.person).count()
	if num in friendship.keys():
		Achievement.objects.update_or_create(
			author=instance.person,
			title=friendship[num],
			defaults={
				'content': 'У вас {0} друзей!'.format(num)
			}
		)


@receiver(signals.post_delete, sender=Friendship)
def delete_on_friendship_delete(instance, *args, **kwargs):
	Friendship.objects.filter(person=instance.friend, friend=instance.person).delete()
	FriendshipRequest.objects\
		.filter(Q(author=instance.person, target=instance.friend) | Q(author=instance.friend, target=instance.person))\
		.delete()
