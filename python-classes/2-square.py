#!/usr/bin/python3

""" Define a Square class. """


class Square:
    """ Represent a square """

    def __init__(self, size=0):
        """ Initializes a Square object with a given size.
        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
