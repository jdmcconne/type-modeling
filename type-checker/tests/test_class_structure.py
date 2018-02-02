# -*- coding: utf-8 -*-

from type_checker import *
from tests.fixtures import TestTypes
import unittest


class TestClassStructure(unittest.TestCase):

    def test_finds_method_by_name(self):
        method = TestTypes.point.method_named("getX")
        self.assertEqual("getX", method.name)

    def test_finds_method_from_supertype(self):
        method = TestTypes.point.method_named("hashCode")
        self.assertEqual("hashCode", method.name)

    def test_finds_method_from_indirect_supertype(self):
        method = TestTypes.rectangle.method_named("hashCode")
        self.assertEqual("hashCode", method.name)

    def test_raises_no_such_method(self):
        with self.assertRaisesRegex(NoSuchMethod, "ergleflopse"):
            TestTypes.point.method_named("ergleflopse")

if __name__ == '__main__':
    unittest.main()
