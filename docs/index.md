# Overview

Track and generate statistics for user access to your Django model instances in your project.

## Table of Contents

  * [Changelog]
  * [Contributing]

## Installation

Install the app into your virtualenv:

    (venv)$ pip install -e git+ssh://git@github.com/ixc/django-access-log.git#egg=django-access-log

Update your settings module:

    INSTALLED_APPS += ('access_log', )

Update your urls.py:

    url(r'^access_log/', include('access_log.urls')),

## Usage

Use the ``log_access`` decorator in your view function. The decorator expects a keyword argument ``model`` to be set to your model class. The associated ``pk`` value for an instance of the model must be supplied as part of the arguments in your view function.

    from access_log.decorators import log_access

    @log_access(model=MyModel)
    @login_required
    def view_func(request, pk):
        # Do something to render the model instance for authenticated user.

To access the statistics for your model:

    >>> from django.contrib.contenttypes.models import ContentType
    >>> from access_log.models import AccessLog
    >>> content_type = ContentType.objects.get_for_model(MyModel)
    >>> stats = AccessLog.objects.stats(content_type)
    >>> stats
    {1: {'content_type': 29, 'count': 5}, 3: {'content_type': 29, 'count': 8}}

The sample output above shows model instance with ``pk`` value of 3 has been accessed 8 times through the decorated view function.

## HTML Docs

Docs are written in [Markdown]. You can use [MkDocs] to build a static HTML
version that you can host anywhere:

    (venv)$ mkdocs build

Or you can use the built-in dev server to preview your documentation as you're
writing it:

    (venv)$ mkdocs serve

It will even auto-reload whenever you save any changes, so all you need to do
to see your latest edits is refresh your browser.

[Changelog]: changelog.md
[Contributing]: contributing.md
[Markdown]: http://daringfireball.net/projects/markdown/
[MkDocs]: http://mkdocs.org
