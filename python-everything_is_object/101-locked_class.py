#!/usr/bin/python3

"""
    This is a module that deal with a locked class
"""


class LockedClass:
    """
        This class prevents user to create new instance attribute dynamically
    """
    __slots__ = ['first_name']

    def __init__(self):
        """
            Method that initializes the instance
        """
        ...
