#!/usr/bin/python3

"""
    This module provides a BaseGeometry class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        This is a subclass of BaseGeometry, represents a rectangle
    """
    def __init__(self, width, height):
        """
            Method that initializes the instance

            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
