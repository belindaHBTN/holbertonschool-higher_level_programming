#!/usr/bin/python3

""" Define a Square class. """


class Square:
    """ Represent a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes a Square object with a given size.
        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Size Getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Size Setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Position Getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ Position Setter """
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError("position must be a tuple of 2 positive "
                                "integers")
        self.__position = value

    def area(self):
        """ Return area of square"""
        return self.size ** 2

    def my_print(self):
        """ Print characters"""
        if self.size == 0:
            print("")
        for row in range(self.size):
            if row == 0:
                for i in range(self.position[1]):
                    print("")
            if self.position[0] > 0:
                for j in range(self.position[0]):
                    print("_", end="")
            for col in range(self.size):
                print("#", end="")
            print("")
