#!/usr/bin/python3

"""Module for testing Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test class"""
    def test_no_id(self):
        """test default id, no prameter """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_id(self):
        """test id with value been pasted in"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_increment_id(self):
        """test id increment"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)
