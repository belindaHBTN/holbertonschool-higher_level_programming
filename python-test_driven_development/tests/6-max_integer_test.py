#!/usr/bin/python3

"""
    Unit test for module 6-max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
        Unit test class for max_integer funtion
    """
    def setUp(self):
        self.max1 = max_integer([1, 2, 3, 4])
        self.max2 = max_integer([1, 3, 4, 2])

    def test_int_list(self):
        self.assertEqual(self.max1, 4)
        self.assertEqual(self.max2, 4)

    def test_None(self):
        self.assertIsNone(max_integer())
