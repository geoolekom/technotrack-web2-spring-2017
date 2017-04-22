from django.contrib import admin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin


class BoundAbleAdmin(admin.StackedInline, GenericInlineModelAdmin):
    ct_field = 'target_content_type'
    ct_fk_field = 'target_id'
    extra = 0
