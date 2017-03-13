from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import viewsets

from api.permissions import IsChatParticipantOrAuthor, IsAuthor, IsAuthorOrReadOnly
from api.serializers import UserSerializer, ChatSerializer, MessageSerializer, CommentSerializer

from chats.models import Chat, Message
from comments.models import Comment


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


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	permission_classes = IsAuthorOrReadOnly,

	def get_queryset(self):
		return self.queryset.prefetch_related('author')

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

