"""
Admin configuration for ``access_log`` app.
"""

# Define `list_display`, `list_filter` and `search_fields` for each model.
# These go a long way to making the admin more usable.

from django.contrib import admin

from access_log import models


class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'content_type', 'object_id',
                    'content_object',)
    list_filter = ('content_type',)
admin.site.register(models.AccessLog, AccessLogAdmin)
