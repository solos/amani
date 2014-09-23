.. amani documentation master file, created by
   sphinx-quickstart on Fri Sep 19 17:27:56 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to amani's documentation!
=================================

About
-----------------------------------------------------------

Amani is a way to patch configuration files.

Install
-----------------------------------------------------------

pip install amani

Usage
-----------------------------------------------------------

constants.py

::

    class A:
        a = 1
        b = []


    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'maps',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '3306',}}


    try:
        import amani
        amani.patch(__file__, globals(), prefix='test')
    except:
        pass

    print A.a
    print A.b
    print DATABASES['default']


test_constants.json

::

        [
            ["A", "a", 2],
            ["A", "b", ["test"]],
            ["DATABASES", "default",
                {
                    "ENGINE": "django.db.backends.mysql",
                    "NAME": "maps",
                    "USER": "user",
                    "PASSWORD": "password",
                    "HOST": "",
                    "PORT": "3306"
                }
            ]
        ]


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
