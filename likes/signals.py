from likes.models import Like
from django.db.models import signals
from notifications.models import Notification


def check_if_unique(instance, *args, **kwargs):
	same_like_exists = Like.objects.filter(
		author_id=instance.author_id,
		target_content_type_id=instance.target_content_type_id,
		target_id=instance.target_id
	).exists()
	if same_like_exists or bool(instance.pk):
		raise ValueError('Переиспользование лайков в другом месте запрещено.')


def notice_on_like(instance, created=False, *args, **kwargs):
	target = instance.target
	if hasattr(target, 'author_id') and created and target.author_id != instance.author_id:
		receiver_id = target.author_id
		content = instance.author.username + ' поставил вам лайк на ' + \
			str(target._meta.verbose_name) + \
			' с id = ' + str(target.id)
		note = Notification(receiver_id=receiver_id, content=content)
		note.save()


def notice_on_like_delete(instance, *args, **kwargs):
	target = instance.target
	if hasattr(target, 'author_id') and target.author_id != instance.author_id:
		receiver_id = target.author_id
		content = instance.author.username + ' убрал лайк с ' + \
			str(target._meta.verbose_name) + \
			' с id = ' + str(target.id)
		note = Notification(receiver_id=receiver_id, content=content)
		note.save()

signals.post_save.connect(notice_on_like, sender=Like)
signals.post_delete.connect(notice_on_like_delete, sender=Like)
signals.pre_save.connect(check_if_unique, sender=Like)