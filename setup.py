import setuptools

from access_log import __version__

setuptools.setup(
    name='access_log',
    version=__version__,
    packages=setuptools.find_packages(),
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
