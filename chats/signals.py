from django.db.models import signals
from django.dispatch import receiver

from chats.models import Chat


@receiver(signals.post_save, sender=Chat)
def add_chat_creator_to_chat(instance, created=False, *args, **kwargs):
	if created:
		instance.participants.add(instance.author)
