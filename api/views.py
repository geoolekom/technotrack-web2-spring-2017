from django.contrib.auth import get_user_model
from chats.models import Chat, Message
from api.serializers import UserSerializer, ChatSerializer, MessageSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from api.permissions import IsChatParticipantOrAuthor, IsAuthor


class UserDetail(RetrieveAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer


class UserList(ListAPIView):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer


class ChatDetail(RetrieveUpdateDestroyAPIView):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer
	permission_classes = (IsChatParticipantOrAuthor, )


class ChatList(ListCreateAPIView):
	queryset = Chat.objects.all()
	serializer_class = ChatSerializer
	permission_classes = (IsChatParticipantOrAuthor, )

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class MessageDetail(RetrieveUpdateDestroyAPIView):
	queryset = Message.objects.all()
	serializer_class = MessageSerializer
	permission_classes = (IsAuthor, )


class MessageList(ListCreateAPIView):
	serializer_class = MessageSerializer
	permission_classes = (IsAuthor, )

	def get_queryset(self):
		return Message.objects.filter(author_id=self.request.user.id)

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)
