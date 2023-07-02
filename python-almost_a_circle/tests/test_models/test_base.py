#!/usr/bin/python3

"""Module for testing Base class"""
import unittest
from models.base import Base


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

    def test_to_json(self):
        """test staticmethod to json"""
        dict1 = {"id": 1, "width": 2}
        dict2 = {"id": 10, "width": 20}
        json_dict1 = Base.to_json_string([])
        self.assertEqual(json_dict1, "[]")
        json_dict2 = Base.to_json_string(None)
        self.assertEqual(json_dict2, "[]")
        str1 = '[{"id": 1, "width": 2}]'
        json_dict3 = Base.to_json_string([dict1])
        self.assertEqual(json_dict3, str1)
        str2 = '[{"id": 1, "width": 2}, {"id": 10, "width": 20}]'
        json_dict4 = Base.to_json_string([dict1, dict2])
        self.assertEqual(json_dict4, str2)

    def tearDown(self):
        """clean up the class private attribute"""
        Base._Base__nb_objects = None
