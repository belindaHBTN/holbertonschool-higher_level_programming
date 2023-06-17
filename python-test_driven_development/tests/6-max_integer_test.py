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
        self.max3 = max_integer([4, 1, 2, 3])
        self.max4 = max_integer([1, -2, 3, 4])
        self.max5 = max_integer([-4, -1, -2, -3])
        self.max6 = max_integer([1])

    def test_int_list(self):
        """ Test for 'max at the end'"""
        self.assertEqual(self.max1, 4)
        """ Test for 'max in the middle'"""
        self.assertEqual(self.max2, 4)
        """ Test for 'max at the beginning'"""
        self.assertEqual(self.max3, 4)

    def test_negtive_int(self):
        """ Test for 'one negative number'"""
        self.assertEqual(self.max4, 4)
        """ Test for 'all number are negative'"""
        self.assertEqual(self.max5, -1)

    def test_one_int(self):
        """ Test for 'one number'"""
        self.assertEqual(self.max6, 1)

    def test_None(self):
        self.assertIsNone(max_integer())
