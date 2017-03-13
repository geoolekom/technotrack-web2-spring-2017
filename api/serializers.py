from rest_framework import serializers
from django.contrib.auth import get_user_model

from chats.models import Chat, Message
from comments.models import Comment
from notifications.models import Notification


class UserSummarySerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('id', 'username', )


class MessageSerializer(serializers.ModelSerializer):
	author = UserSummarySerializer(read_only=True)

	class Meta:
		model = Message
		fields = ('id', 'author', 'chat', 'pub_time', 'upd_time', 'content', )


class ChatSerializer(serializers.ModelSerializer):
	# message_set = MessageSerializer(many=True, read_only=True)
	# participants = UserSummarySerializer(many=True, read_only=True)
	author = UserSummarySerializer(read_only=True)

	class Meta:
		model = Chat
		fields = ('id', 'author', 'title', 'participants', 'message_set',)


class NotificationSerializer(serializers.ModelSerializer):
	receiver = UserSummarySerializer(read_only=True)

	class Meta:
		model = Notification
		fields = ('id', 'receiver', 'content', )


class UserSerializer(serializers.ModelSerializer):
	# chat_set = ChatSummarySerializer(many=True)
	# notification_set = NotificationSummarySerializer(many=True)

	class Meta:
		model = get_user_model()
		fields = ('id', 'username', 'email', 'first_name', 'last_name', 'chat_set', 'notification_set', )


class CommentSerializer(serializers.ModelSerializer):

	author = UserSummarySerializer(read_only=True)

	class Meta:
		model = Comment
		fields = ('id', 'author', 'content', )
