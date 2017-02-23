from django.contrib import admin
from comments.models import Comment
from core.admin import BoundAbleAdmin
from likes.admin import LikesInline


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	inlines = LikesInline,


class CommentsInline(BoundAbleAdmin):
	model = Comment
