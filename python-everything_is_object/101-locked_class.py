#!/usr/bin/python3

"""
    This is a module that deal with a locked class
"""


class LockedClass:
    """
        This class prevents user to create new instance attribute dynamically
    """
    __slots__ = ['first_name']

    def __init__(self, first_name):
        self.first_name = first_name
