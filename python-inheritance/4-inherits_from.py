#!/usr/bin/python3

"""
    This module provides a inherits_from function.
"""


def inherits_from(obj, a_class):
    """
        Function that determine if the obj is an instance of the class that
        inherited (directly or indirectly) from the specified class

        Args:
        obj: the instance
        a_class: the class

        Returns:
        True:  if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        False: otherwise
    """
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
