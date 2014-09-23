#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append('..')

import unittest
import amani


class A:

    a = 1
    b = []

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


class DefaultTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_patch_class(self):
        try:
            g = globals()
            patches = amani.patch(__file__, g)
            self.assertEqual(A.a, 2)
            self.assertEqual(A.b, ['test'])
            self.assertEqual(DATABASES['default']['USER'], 'user')
            self.assertEqual(DATABASES['default']['PASSWORD'], 'password')
        except Exception, e:
            print 'e', e


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultTestCase('test_patch_class'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite', verbosity=2)
