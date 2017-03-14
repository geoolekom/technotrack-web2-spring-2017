from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import viewsets

from api.permissions import IsChatParticipantOrAuthor, IsAuthor, IsAuthorOrReadOnly, IsAdminOrReadOnly, IsConsumer
from api.serializers import UserSerializer, LikeSerializer, \
	ChatSerializer, MessageSerializer, \
	CommentSerializer, PostSerializer, \
	AchievementSerializer, NotificationSerializer

from chats.models import Chat, Message
from comments.models import Comment
from feed.models import Post
from achievements.models import Achievement
from notifications.models import Notification
from likes.models import Like


class UserViewSet(viewsets.ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer


class ChatViewSet(viewsets.ModelViewSet):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer
	permission_classes = IsChatParticipantOrAuthor,

	def get_queryset(self):
		uid = self.request.user.id
		return Chat.objects.filter(Q(author_id=uid) | Q(participants__id=uid)).prefetch_related('author')

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer
	permission_classes = (IsAuthor,)

	def get_queryset(self):
		return Message.objects.filter(
			Q(author_id=self.request.user.id) | Q(chat_id__in=self.request.user.chat_set.all())
		).prefetch_related('author')

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class NotificationViewSet(viewsets.ModelViewSet):
	queryset = Notification.objects.all()
	serializer_class = NotificationSerializer
	permission_classes = IsConsumer,

	def get_queryset(self):
		return self.queryset.filter(consumer_id=self.request.user.id).prefetch_related('consumer')


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = IsAuthorOrReadOnly,

	def get_queryset(self):
		return self.queryset.prefetch_related('author')

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = IsAuthorOrReadOnly,

	def get_queryset(self):
		return self.queryset.prefetch_related('author')

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class AchievementViewSet(viewsets.ModelViewSet):
	queryset = Achievement.objects.all()
	serializer_class = AchievementSerializer
	permission_classes = IsAdminOrReadOnly,

	def get_queryset(self):
		return self.queryset.prefetch_related('author')


class LikeViewSet(viewsets.ModelViewSet):
	queryset = Like.objects.all()
	serializer_class = LikeSerializer
	permission_classes = IsAuthorOrReadOnly,



