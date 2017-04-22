from django.contrib import admin
from chats.models import Chat, Message
from django.contrib.auth import get_user_model


@admin.register(Message)
class MessagesAdmin(admin.ModelAdmin):
    pass


class MessagesInline(admin.StackedInline):
    model = Message
    extra = 0


@admin.register(Chat)
class ChatsAdmin(admin.ModelAdmin):
    inlines = MessagesInline,


class ChatsInline(admin.StackedInline):
    model = get_user_model().chat_set.through
    extra = 0
