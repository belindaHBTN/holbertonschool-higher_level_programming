#!/usr/bin/python3

"""
    This is a module that deal with rectangle
"""


class Rectangle:
    """
        This is a class that defines a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Method that initializes the instance

            Args:
                width: width of the rectangle
                height: height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return 0

        return self.width * 2 + self.height * 2

    def __str__(self):
        """
            Method that return the rectangle
        """
        rectangle = ""

        if self.width == 0 or self.height == 0:
            return ""

        for i in range(self.height):
            for j in range(self.width):
                rectangle = rectangle + str(self.print_symbol)
            rectangle = rectangle + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """
            Method that return the instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
            Method that delete the instance and print a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Method that return the bigger rectangle
        """
        if not isinstance(rect_1, Ractangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Ractangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
