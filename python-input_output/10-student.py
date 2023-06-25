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

    def to_json(self, attrs=None):
        """ Function that retrieves a dictionary representation of an instance
        Args:
            obj: an instance of a Class
            attrs: if it is a list of strings or not

        Return:
            a dictionary
        """
        student_dict = self.__dict__

        if type(attrs) is not list:
            return student_dict
        else:
            dict = {}
            for attr in attrs:
                for el in student_dict:
                    if el == attr:
                        dict[el] = student_dict[el]
            return dict
