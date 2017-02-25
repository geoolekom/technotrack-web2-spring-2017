from django.db.models import signals
from notifications.models import Notification
from achievements.models import Achievement, friendship
from relations.models import FriendshipRequest, Friendship


def add_friendship_if_accepted(instance, created=False, *args, **kwargs):
	if instance.accepted:
		Friendship.objects.create(person=instance.author, friend=instance.target)


def note_on_friendship_request(instance, created=False, *args, **kwargs):
	if created:
		Notification.objects.create(
			consumer=instance.target,
			content='{0} хочет с вами подружиться'.format(instance.author.username)
		)


def achieve_on_friendship(instance, created=False, *args, **kwargs):
	num = Friendship.objects.filter(person=instance.person).count()
	if num in friendship.keys():
		Achievement.objects.create(
			author=instance.person,
			title=friendship[num],
			content='У вас {0} друзей!'.format(num)
		)

signals.post_save.connect(note_on_friendship_request, sender=FriendshipRequest)
signals.post_save.connect(add_friendship_if_accepted, sender=FriendshipRequest)
signals.post_save.connect(achieve_on_friendship, sender=Friendship)
