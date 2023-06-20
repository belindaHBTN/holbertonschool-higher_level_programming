#!/usr/bin/python3

"""
    This module provides a is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
        Function that determine if the obj is an instance of the class

        Args:
        obj: the instance
        a_class: the class

        Returns:
        True: if the object is an instance of class or is an instance of a
              class that inherited from
        False: otherwise
    """
    return isinstance(obj, a_class)
