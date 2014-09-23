#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import amani

setup(name='amani',
      version=amani.__version__,
      description='A way to patch configuration files.',
      long_description=amani.__doc__,
      author=amani.__author__,
      author_email='solos@solos.so',
      py_modules=['amani'],
      scripts=['amani.py'],
      license='MIT',
      platforms=['any'],
      url='https://github.com/solos/amani')
