Installation
============

Basic Installation
------------------
Install {{cookiecutter.project_name}} with :command:`pip`::

    $ pip install {{cookiecutter.project_name}}

Django Settings
---------------
You have to add the app to your installed apps in your Django settings

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'juntagrico',
        '{{cookiecutter.project_slug}}',
    ]
    
You also have to configure caching so that the app works correctly, and you have to execute the django createcachetable command (during the command juntagrico and all juntagrico apps have to be removed from the INSTALLED_APPS).

.. code-block:: python

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'juntagrico_app_cache_table',
            'TIMEOUT': None,
        }
    }
