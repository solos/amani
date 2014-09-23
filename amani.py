#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'solos'


def patch(abspath, g, prefix='test'):
    try:
        import os
        import json
        import traceback
        from inspect import isclass
        absdir, basename = os.path.split(os.path.realpath(abspath))
        barename, suffix = os.path.splitext(basename)
        patch_file = '{absdir}/{prefix}_{barename}.json'.format(**locals())
        patches = json.loads(file(patch_file).read())
        for (name, key, value) in patches:
            if name in g:
                if isinstance(g[name], (unicode, basestring, list)):
                    g[name] = value
                elif isclass(g[name]):
                    setattr(g[name], key, value)
                elif isinstance(g[name], dict):
                    g[name][key] = value
                elif isinstance(g[name], tuple):
                    g[name] = tuple(value)
                elif isinstance(g[name], set):
                    g[name] = set(value)
        return patches
    except:
        print traceback.format_exc()
