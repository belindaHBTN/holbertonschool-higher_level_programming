#!/usr/bin/python3

"""
This module provides a function that prints a square.
"""


def print_square(size):
    """
    Print a square with #.

    Arg:
    size: the size of the square.

    Return:
    No return.

    Raises:
    TypeError: If the argument is not an integer
    TypeError: If the argument is a float and is less than 0
    ValueError: If the argument is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    square = ['#' * size for _ in range(size)]
    for row in square:
        print(row)
