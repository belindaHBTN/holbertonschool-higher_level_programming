#!/usr/bin/python3

"""
    This is a module contain a Base class
"""


class Base:
    """
        This is a Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize an instance of class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
