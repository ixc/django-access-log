"""
Models for ``access_log`` app.
"""

from django.contrib.contenttypes.models import ContentType
from functools import wraps
from .models import AccessLog


def log_access(function=None, model=None):
    """
    Decorator to log user access to an instance of the specified model class.
    ``pk`` must exists in the list of keyword arguments to identify the
    affected instance.
    """
    def actual_decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if model:
                pk = kwargs.get('pk', None)
                obj = None
                if model and pk:
                    obj = model.objects.get(pk=pk)
                    ct = ContentType.objects.get_for_model(obj.__class__)
                    access_log = AccessLog(
                        user=request.user, content_type=ct, object_id=obj.pk)
                    access_log.save()
            return view_func(request, *args, **kwargs)
        return wrapper
    if function:
        return actual_decorator(function)
    return actual_decorator
