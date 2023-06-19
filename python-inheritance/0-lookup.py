#!/usr/bin/python3

def lookup(obj):
    """Function that returns the list of available attributes and methods.

    Args:
        obj: the instance of the class

    Returns:
        The list of attributes and methods of an obj
    """
    return dir(obj)
