#!/usr/bin/python3

"""
    This module provides a BaseGeometry class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        This is a subclass of Rectangle, represents a square
    """
    def __init__(self, size):
        """
            Method that initializes a square instance

            Arg:
                size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            Method to calculate the area of the geometry
        """
        return self.__size ** 2

    def __str__(self):
        """
            Method to generate output for end user
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
