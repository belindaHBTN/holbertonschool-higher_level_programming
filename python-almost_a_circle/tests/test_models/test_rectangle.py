#!/usr/bin/python3

"""Module for testing Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """test class"""
    def setUp(self):
        """reset the base class private attribute"""
        Base._Base__nb_objects = 0

    def test_rectangle_exist(self):
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

    def test_validate_attr(self):
        """test the validation of the attributes"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2, 3, 4)
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, "2", 3, 4)
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, "3", 4)
        with self.assertRaises(TypeError):
            r4 = Rectangle(10, 2, 3, "4")
        with self.assertRaises(ValueError):
            r5 = Rectangle(-10, 2, 3, 4)
        with self.assertRaises(ValueError):
            r6 = Rectangle(0, 2, 3, 4)
        with self.assertRaises(ValueError):
            r7 = Rectangle(10, -2, 3, 4)
        with self.assertRaises(ValueError):
            r8 = Rectangle(10, 0, 3, 4)
        with self.assertRaises(ValueError):
            r9 = Rectangle(10, 2, -3, 4)
        with self.assertRaises(ValueError):
            r10 = Rectangle(10, 2, 3, -4)

    def test_area(self):
        """test the area method of the instance of rectangle class"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_print1(self):
        """test the rectangle instance's print out'"""
        r1 = Rectangle(2, 3)
        output = StringIO()
        expected_output = "##\n##\n##\n"
        import sys
        sys.stdout = output
        r1.display()
        printed_output = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output, expected_output)

    def test_print2(self):
        """test the rectangle instance's print out'"""
        r2 = Rectangle(2, 3, 2, 2)
        output = StringIO()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        import sys
        sys.stdout = output
        r2.display()
        printed_output = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(printed_output, expected_output)

    def test_str(self):
        """test the str method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        """test the update method"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def tearDown(self):
        """clean up the class private attribute"""
        Base._Base__nb_objects = None
