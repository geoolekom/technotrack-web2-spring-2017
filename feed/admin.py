from django.contrib import admin
from feed.models import Post
from comments.admin import CommentsInline
from likes.admin import LikesInline


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	inlines = CommentsInline, LikesInline,
