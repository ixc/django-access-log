"""
URLconf for ``access_log`` app.
"""

# Prefix URL names with the app name. Avoid URL namespaces unless it is likely
# this app will be installed multiple times in a single project.

from django.conf.urls import include, patterns, url

urlpatterns = patterns(
    'access_log.views',

    url(r'^downloads/(?P<content_type>\d+)/$',
        'downloads',
        name='access_log_downloads'),

    url(r'^downloads/(?P<content_type>\d+)/(?P<object_id>\d+)/$',
        'downloads',
        name='access_log_downloads'),
)
