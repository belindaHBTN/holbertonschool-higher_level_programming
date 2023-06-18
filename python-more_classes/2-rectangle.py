#!/usr/bin/python3

"""
    This is a module that deal with rectangle
"""


class Rectangle:
    """
        This is a class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
            Method that initializes the instance

            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Method that calculate the rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
            Method that calculate the perimeter of the rectangle
        """
        return self.width * 2 + self.height * 2
