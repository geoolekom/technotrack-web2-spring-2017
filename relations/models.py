from django.db import models
from core.models import Authored
from django.conf import settings


class FriendshipRequest(models.Model, Authored):
	target = models.ForeignKey(settings.AUTH_USER_MODEL)
	accepted = models.BooleanField()


class Friendship(models.Model):
	first = models.ForeignKey(settings.AUTH_USER_MODEL)
	second = models.ForeignKey(settings.AUTH_USER_MODEL)