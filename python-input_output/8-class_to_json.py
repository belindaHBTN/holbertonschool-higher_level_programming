#!/usr/bin/python3
"""
    This module contains a function that returns the dictionary description
    with simple data structure
"""


def class_to_json(obj):
    """ Function that return a dictionary description with data structure

    Args:
      obj: an instance of a Class

    Return:
        a dictionary
    """
    return obj.__dict__
