#!/usr/bin/python3

"""
    This module provides a is_same_class function.
"""


def is_same_class(obj, a_class):
    """
        Function that determine if the obj is an instance of the class

        Args:
        obj: the instance
        a_class: the specified class

        Returns:
        True: if the object is exactly an instance of the specified class
        False: otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
