#!/usr/bin/python3

"""
This module provides a function that prints a full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print ou the full name.

    Args:
    first_name: The first name.
    last_name: The last name.

    Returns:
    No return.

    Raises:
    TypeError: If any of the argument isn't a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
