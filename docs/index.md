# Overview

Track and generate statistics for of user access to your Django model instances in your project.

## Table of Contents

  * [Changelog]
  * [Contributing]

## Installation

Install the app into your virtualenv:

    (venv)$ pip install -e git+ssh://git@github.com/ixc/django-access-log.git#egg=django-access-log

Update your settings module:

    INSTALLED_APPS += ('access_log', )

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
