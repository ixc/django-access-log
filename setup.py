from __future__ import print_function

import setuptools
import sys

version = '0.1.dev0'

# Convert README.md to reStructuredText.
if {'bdist_wheel', 'sdist'}.intersection(sys.argv):
    try:
        import pypandoc
    except ImportError:
        print('ERROR: You must install `pypandoc` to convert `README.md` to '
              'reStructuredText to use as long description.',
              file=sys.stderr)
        exit(1)
    print('Converting `README.md` to reStructuredText to use as long '
          'description.')
    long_description = pypandoc.convert('README.md', 'rst')

setuptools.setup(
    name='django-access-log',
    version=version,
    author='Interaction Consortium',
    author_email='studio@interaction.net.au',
    url='https://github.com/ixc/django-access-log',
    description='Track and generate statistics for user access to your Django '
                'model instances in your project.',
    long_description=locals().get('long_description', ''),
    license='MIT',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'coverage',
        'django-dynamic-fixture',
        'django-nose',
        'django-webtest',
        'mkdocs',
        'mock',
        'nose-progressive',
        'tox',
        'WebTest',
    ],
    extras_require={
        'dev': ['ipdb', 'ipython'],
        'postgres': ['psycopg2'],
    },
)
