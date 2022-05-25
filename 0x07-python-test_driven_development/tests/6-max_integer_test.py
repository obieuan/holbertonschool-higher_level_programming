#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Pruebas """

    def test_if_list(self):
        self.normlist = [1, 2, 3, 4]
        self.assertIsInstance(self.normlist, list)

    def test_builtin_max(self):
        self.toughlist = [1, 90, 2, 13, 34, 5, -13, 3]
        self.assertEqual(max_integer(self.toughlist), max(self.toughlist))

    def test_max_int_basic(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_int_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_int_neg(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_int_one(self):
        self.assertEqual(max_integer([1]), 1)

if __name__ == '__main__':
    unittest.main()
