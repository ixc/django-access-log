"""
Models for ``access_log`` app.
"""

# Compose concrete models from abstract models and mixins, to facilitate reuse.

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Count
from django.utils import timezone


class AbstractBaseModel(models.Model):
    """
    Abstract base model with common fields and methods for all models.

    Add ``created`` and ``modified`` timestamp fields. Update the ``modified``
    field automatically on save. Sort by primary key.
    """
    created = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False)
    modified = models.DateTimeField(
        default=timezone.now, db_index=True, editable=False)

    class Meta:
        abstract = True
        get_latest_by = 'pk'
        ordering = ('-id', )

    def save(self, *args, **kwargs):
        """
        Update ``self.modified``.
        """
        self.modified = timezone.now()
        super(AbstractBaseModel, self).save(*args, **kwargs)


class AccessLogManager(models.Manager):
    """
    Adds aggregation method to return access log statistics for the specified
    content type.
    """
    def stats(self, content_type, object_id=None):
        """
        Returns dict containing number of downloads for each object of the same
        content type.
        """
        objs = self.filter(content_type=content_type)
        if object_id:
            objs = objs.filter(object_id=object_id)

        objs = objs \
            .values('object_id', 'content_type') \
            .annotate(Count('object_id')) \
            .order_by()

        return {obj['object_id']: {
            'count': obj['object_id__count'],
            'content_type': obj['content_type'],
        } for obj in objs}


class AccessLog(AbstractBaseModel):
    """
    Model to log access to restricted objects.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    objects = AccessLogManager()

    def __str__(self):
        return '%s: %d' % (self.content_type, self.object_id)
