#!/usr/bin/env python
# -*- coding: utf-8 -*-


class A:

    a = 1
    b = []
    c = [1, 3, 5]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'maps',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
    }
}

try:
    import amani
    g = globals()
    amani.patch(__file__, g)
except:
    pass
