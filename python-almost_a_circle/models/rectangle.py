#!/usr/bin/python3

"""
    This module include a Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
        This is a class represent Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialises an instance
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
            x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            x setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
            y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
            calculate the area of the rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
            prints in stdout the rectangle instance with the character #
        """
        for y in range(self.y):
            print()
        for height in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
            print out specific content
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}" \
            f" - {self.width}/{self.height}"

    def update(self, *args):
        """
            assign an argument to each attribute
        """
        key = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, key[i], args[i])
