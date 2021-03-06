"""
App configuration for ``access_log`` app.
"""

# Register signal handlers, but avoid interacting with the database.
# See: https://docs.djangoproject.com/en/1.8/ref/applications/#django.apps.AppConfig.ready

from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'access_log'
    verbose_name = 'Access Log'
