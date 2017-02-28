from django.test import TestCase
from django.contrib.auth import get_user_model, hashers

from feed.models import Post
from relations.models import Friendship


class TestFeed(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create(username='test', password=hashers.make_password('test'))
		self.other = get_user_model().objects.create(username='other', password=hashers.make_password('other'))
		self.friendship = Friendship.objects.create(person=self.user, friend=self.other)

	def testFeedElementOnNotification(self):
		assert self.user.feedelement_set.count() == 1

	def testFeedElementOnPost(self):
		Post.objects.create(title='title', content='content', author=self.other)
		assert self.user.feedelement_set.count() == 2

	def tearDown(self):
		self.friendship.delete()
		self.user.delete()
		self.other.delete()

