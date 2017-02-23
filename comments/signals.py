from django.db.models import signals
from comments.models import Comment
from notifications.models import Notification


def notice_on_comment(instance, created=False, *args, **kwargs):
	target = instance.target
	if hasattr(target, 'author_id') and created and target.author_id != instance.author_id:
		receiver_id = target.author_id
		content = instance.author.username + ' прокомментировал ' + \
			str(target._meta.verbose_name) + \
			' с id = ' + str(target.id)
		note = Notification(receiver_id=receiver_id, content=content)
		note.save()


signals.post_save.connect(notice_on_comment, sender=Comment)
