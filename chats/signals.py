from django.db.models import signals
from chats.models import Chat


def add_chat_creator_to_chat(instance, created=False, *args, **kwargs):
	if created:
		instance.participants.add(instance.author)


signals.post_save.connect(add_chat_creator_to_chat, sender=Chat)
