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
    
