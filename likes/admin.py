from django.contrib import admin
from likes.models import Like
from core.admin import BoundAbleAdmin


@admin.register(Like)
class LikesAdmin(admin.ModelAdmin):
    pass


class LikesInline(BoundAbleAdmin):
    model = Like
