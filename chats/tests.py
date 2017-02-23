from django.test import TestCase
from django.contrib.auth import get_user_model, hashers
from chats.models import Chat


class TestLikes(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create(username='test', password=hashers.make_password('test'))
		self.chat = Chat.objects.create(title='title', author=self.user)

	def testChatContainsCreator(self):
		assert self.chat.participants.get() == self.user

	def tearDown(self):
		self.user.delete()
		self.chat.delete()
