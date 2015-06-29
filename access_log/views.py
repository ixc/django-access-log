"""
Views for ``access_log`` app.
"""

# Do not use generic class based views unless there is a really good reason to.
# Functional views are much easier to comprehend and maintain.

from django.template.response import TemplateResponse
from .models import AccessLog


def downloads(request, content_type, object_id=None):
    downloads = AccessLog.objects.filter(content_type=content_type)
    if object_id:
        downloads = downloads.filter(object_id=object_id)
    downloads = downloads.order_by('-created')
    context = {
        'downloads': downloads,
    }
    return TemplateResponse(request, 'access_log/downloads.html', context)
