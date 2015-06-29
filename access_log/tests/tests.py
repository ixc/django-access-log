"""
Tests for ``access_log`` app.
"""

# WebTest API docs: http://webtest.readthedocs.org/en/latest/api.html

from django.core.urlresolvers import reverse
from django_dynamic_fixture import G
from django_webtest import WebTest

from access_log import forms, models, views
from access_log.tests import models as test_models


class Forms(WebTest):
    def test(self):
        pass


class Models(WebTest):
    def test_BaseModel(self):
        """
        Test that ``modified`` field is updated on save.
        """
        obj = G(test_models.BaseModel)
        modified = obj.modified
        obj.save()
        self.assertNotEqual(obj.modified, modified)


class Views(WebTest):
    def test_downloads(self):
        response = self.app.get(reverse('access_log_downloads', args=[1]))
        response.mustcontain('table')

        response = self.app.get(reverse('access_log_downloads', args=[1, 2]))
        response.mustcontain('table')
