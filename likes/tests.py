from django.test import TestCase
from likes.models import Like
from feed.models import Post
from django.contrib.auth import get_user_model, hashers


class TestLikes(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create(username='test', password=hashers.make_password('test'))
		self.other = get_user_model().objects.create(username='other', password=hashers.make_password('other'))
		self.post = Post.objects.create(title='title', content='content', author=self.user)

	def testLikeImmutability(self):
		with self.assertRaises(ValueError):
			like = Like.objects.create(author=self.user, target=self.post)
			like.save()

	def testSelfLikeNotifications(self):
		Like.objects.create(author=self.user, target=self.post)
		assert self.user.notification_set.count() == 0

	def testOtherLikeNotifications(self):
		Like.objects.create(author=self.other, target=self.post)
		assert self.user.notification_set.count() == 1

	def tearDown(self):
		self.user.delete()
		self.other.delete()
		self.post.delete()
