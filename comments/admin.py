from django.contrib import admin
from comments.models import Comment
from core.admin import BoundAbleAdmin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass


class CommentsInline(BoundAbleAdmin):
	model = Comment
