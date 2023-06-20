#!/usr/bin/python3

"""
    Module that including a class.
"""


class MyList(list):
    """
    A class that inheritance from built-in class list
    """
    def print_sorted(self):
        """Function that print the sorted list.
        """
        print(sorted(self))
