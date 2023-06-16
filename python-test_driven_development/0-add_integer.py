#!/usr/bin/python3

"""
This module provides a function for adding two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result.

    Args:
    a: The first number.
    b: The second number.

    Returns:
    int: The sum of the two numbers.

    Raises:
    TypeError: If a or b aren't integer or float numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
