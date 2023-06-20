#!/usr/bin/python3

"""
    This module provides a BaseGeometry class.
"""


class BaseGeometry:
    """
        This is a class with Geometry
    """
    def area(self):
        """
            Public instance method to raise an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Public instance method to validates value

            Args:
            name: always a string
            value: the value need to be validated

            Errors:
            TypeError: value is not an integer
            ValueError: value is equal or less than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
