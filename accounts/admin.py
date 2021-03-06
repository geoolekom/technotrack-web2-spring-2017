from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from chats.admin import ChatsInline, Chat
from notifications.admin import NotificationsInline
from achievements.admin import AchievementsInline


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    inlines = ChatsInline, NotificationsInline, AchievementsInline


class AccountsInline(admin.StackedInline):
    model = Chat.participants.through
    extra = 0
