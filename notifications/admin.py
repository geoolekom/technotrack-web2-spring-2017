from django.contrib import admin
from notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
	pass


class NotificationsInline(admin.TabularInline):
	model = Notification
	extra = 0
