#!/usr/bin/python3

"""Module for testing Square class"""
import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    """test class"""
    def setUp(self):
        """reset the base class private attribute"""
        Base._Base__nb_objects = 0

    def test_square_exist(self):
        """test square exist"""
        s1 = Square(1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        s2 = Square(1, 2)
        self.assertEqual(s2.width, 1)
        self.assertEqual(s2.height, 1)
        self.assertEqual(s2.x, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.width, 1)
        self.assertEqual(s3.height, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        s4 = Square(1, 2, 3, 99)
        self.assertEqual(s4.width, 1)
        self.assertEqual(s4.height, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)
        self.assertEqual(s4.id, 99)

    def test_attrs_validation(self):
        """test the validation of the attributes"""
        with self.assertRaises(TypeError):
            s1 = Square("1")
        with self.assertRaises(TypeError):
            s2 = Square(1, "2")
        with self.assertRaises(TypeError):
            s3 = Square(1, 2, "3")
        with self.assertRaises(ValueError):
            s4 = Square(-1)
        with self.assertRaises(ValueError):
            s5 = Square(1, -2)
        with self.assertRaises(ValueError):
            s6 = Square(1, 2, -3)
        with self.assertRaises(ValueError):
            s7 = Square(0)

    def test_str(self):
        """test the str method"""
        s1 = Square(3, 1, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 1/3 - 3")

    def test_size(self):
        """test the getter and setter of size attribute"""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        with self.assertRaises(TypeError):
            s1.size = "9"
        with self.assertRaises(ValueError):
            s1.size = -1

    def test_update(self):
        """test update method"""
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update()
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/0 - 5")
        s1.update(89, 1)
        self.assertEqual(s1.__str__(), "[Square] (89) 0/0 - 1")
        s1.update(89, 1, 2)
        self.assertEqual(s1.__str__(), "[Square] (89) 2/0 - 1")
        s1.update(89, 1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (89) 2/3 - 1")
        s1.update(id=98)
        self.assertEqual(s1.__str__(), "[Square] (98) 2/3 - 1")
        s1.update(id=98, y=20)
        self.assertEqual(s1.__str__(), "[Square] (98) 2/20 - 1")
        s1.update(id=98, y=20, size=15)
        self.assertEqual(s1.__str__(), "[Square] (98) 2/20 - 15")
        s1.update(id=98, y=20, size=15, x=3)
        self.assertEqual(s1.__str__(), "[Square] (98) 3/20 - 15")

    def test_to_dictionary(self):
        """test to_dictionary method"""
        s1 = Square(10, 2, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/1 - 10")
        s1_dict = s1.to_dictionary()
        self.assertEqual(s1_dict, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
