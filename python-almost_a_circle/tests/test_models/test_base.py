#!/usr/bin/python3

"""Module for testing Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """test class"""
    def setUp(self):
        """reset the class private attribute"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """test id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_rectangle(self):
        """test rectangle exist"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10, 4)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(2, 10, 6, 4)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 10)
        self.assertEqual(r3.x, 6)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 3)
        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 2)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)
        self.assertEqual(r4.id, 12)

    def tearDown(self):
        """clean up the class private attribute"""
        Base._Base__nb_objects = None
