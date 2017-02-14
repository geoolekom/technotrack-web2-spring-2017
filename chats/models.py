from django.db import models
from core.models import Authored


class Chat(models.Model, Authored):
	pass


class Message(models.Model):
	chat = models.ForeignKey(Chat)
	content = models.TextField()

