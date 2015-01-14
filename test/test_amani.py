#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
sys.path.append('..')

import unittest
from constants import A
from constants import DATABASES


class DefaultTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_patch_class(self):
        self.assertEqual(A.a, 2)
        self.assertEqual(A.b, ['test'])
        self.assertEqual(A.c[1], 2**32)
        self.assertEqual(DATABASES['default']['USER'], 'username')
        self.assertEqual(DATABASES['default']['PASSWORD'], 'pass-WORD')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(DefaultTestCase('test_patch_class'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite', verbosity=2)
