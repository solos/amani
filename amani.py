#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'solos'

import os
import imp
from inspect import isclass
from collections import deque


def patch(abspath, g, prefix='patch'):
    patches = []
    absdir, basename = os.path.split(os.path.realpath(abspath))
    barename, suffix = os.path.splitext(basename)
    module_name = '{prefix}_{barename}'.format(**locals())
    fp, pathname, desc = imp.find_module(module_name)
    try:
        module = imp.load_module(module_name, fp, pathname, desc)
        patches = module.PATCHES
    except Exception, e:
        print e
        patches = []
    finally:
        if fp:
            fp.close()
    for i in patches:
        patch = deque(i)
        name = patch.popleft()
        temp = g[name]
        rpatch(temp, patch)


def rpatch(temp, patch):
    length = len(patch)
    if length > 2:
        key = patch.popleft()
        if isinstance(temp, dict) or isinstance(key, int):
            temp = temp[key]
        elif isclass(temp):
            temp = getattr(temp, key)
        rpatch(temp, patch)
    elif length == 2:
        key = patch.popleft()
        value = patch.popleft()
        if isinstance(key, int) or isinstance(temp, dict):
            temp[key] = value
        elif isclass(temp):
            setattr(temp, key, value)
    else:
        return
