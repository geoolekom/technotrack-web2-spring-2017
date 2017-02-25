from django.contrib import admin
from achievements.models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
	pass


class AchievementsInline(admin.TabularInline):
	model = Achievement
	extra = 0
