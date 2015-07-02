"""
Tests for ``access_log`` app.
"""

# WebTest API docs: http://webtest.readthedocs.org/en/latest/api.html

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from django_dynamic_fixture import G
from django_webtest import WebTest
from mock import Mock


from . import models as test_models
from .. import decorators, forms, models, views


class Forms(WebTest):
    def test(self):
        pass


class Models(WebTest):
    def setUp(self):
        self.logged_model = test_models.BaseModel
        user_model = get_user_model()
        self.user = G(user_model)

    def test_logged_model(self):
        """
        Test that ``modified`` field is updated on save.
        """
        obj = G(self.logged_model)
        modified = obj.modified
        obj.save()
        self.assertNotEqual(obj.modified, modified)

    def test_log_access(self):
        """
        Test that an instance of ``AccessLog`` is created by the decorator.
        """
        obj = self.logged_model()
        obj.save()

        view_func = Mock()
        view_func.__name__ = 'view_func'
        request = RequestFactory()
        request.user = self.user
        decorated_func = decorators.log_access(view_func,
                                               model=self.logged_model)
        decorated_func(request, pk=obj.pk)

        log_entry = models.AccessLog.objects.get(object_id=obj.pk)
        self.assertEqual(log_entry.user, self.user)


class Views(WebTest):
    def test_downloads(self):
        response = self.app.get(reverse('access_log_downloads', args=[1]))
        self.assertEqual(response.status_code, 302)
