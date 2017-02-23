from rest_framework import serializers
from django.contrib.auth import get_user_model
from chats.models import Chat, Message
from notifications.models import Notification
from django.forms.models import model_to_dict
import collections


class UserSummarySerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('id', 'username', )


class MessageSerializer(serializers.ModelSerializer):
	author = UserSummarySerializer(read_only=True)

	class Meta:
		model = Message
		fields = ('id', 'author', 'chat', 'pub_time', 'upd_time', 'content', )


class ChatSummarySerializer(serializers.ModelSerializer):
	author = UserSummarySerializer(read_only=True)
	last_message = MessageSerializer(source='message_set.latest', read_only=True, required=False)

	def to_representation(self, instance):
		try:
			result = super(ChatSummarySerializer, self).to_representation(instance)
			return result
		except Message.DoesNotExist:
			result = collections.OrderedDict(model_to_dict(instance, exclude=['participants', 'author']))
			result.update({
				'last_message': None,
				'author': {
					'id': instance.author.id,
					'username': instance.author.username
				},
			})
			return result

	class Meta:
		model = Chat
		fields = ('id', 'title', 'author', 'last_message', )


class ChatSerializer(serializers.ModelSerializer):
	message_set = MessageSerializer(many=True, read_only=True)
	participants = UserSummarySerializer(many=True, read_only=True)
	author = UserSummarySerializer(read_only=True)

	class Meta:
		model = Chat
		fields = ('id', 'author', 'title', 'participants', 'message_set',)


class NotificationSummarySerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		fields = ('id', 'content', )


class NotificationSerializer(serializers.ModelSerializer):
	receiver = UserSummarySerializer(read_only=True)

	class Meta:
		model = Notification
		fields = ('id', 'content', 'receiver', )


class UserSerializer(serializers.ModelSerializer):
	chat_set = ChatSummarySerializer(many=True)
	notification_set = NotificationSummarySerializer(many=True)

	class Meta:
		model = get_user_model()
		fields = ('id', 'username', 'email', 'first_name', 'last_name', 'chat_set', 'notification_set', )

