#!/usr/bin/python3

""" Define a Square class. """


class Square:
    """ Represent a square """

    def __init__(self, size=0):
        """ Initializes a Square object with a given size.
        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    @property
    def size(self):
        """ Size Getter"""
        return self.__size

    @size.setter
    def size(self, size):
        """ Size Setter"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return area of square"""
        return self.__size ** 2

    def my_print(self):
        """ Print the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
