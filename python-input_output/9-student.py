#!/usr/bin/python3
"""
    This module contains a Student class
"""


class Student:
    """
        A class that represent student
    """
    def __init__(self, first_name, last_name, age):
        """
            initialise an instance of student Class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Function that retrieves a dictionary representation of an instance
        Args:
            obj: an instance of a Class

        Return:
            a dictionary
        """
        return self.__dict__
