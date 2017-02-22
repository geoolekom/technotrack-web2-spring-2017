from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin
from .models import User


class BoundAbleAdmin(admin.StackedInline, GenericInlineModelAdmin):
    ct_field = 'target_content_type'
    ct_fk_field = 'target_id'
    extra = 0


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass
