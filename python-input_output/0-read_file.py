#!/usr/bin/python3
"""
    This module contains a function that read text from a file
"""

def read_file(filename=""):
    """ Function tha tread text from a file

    Args:
        filename: optional arg, filename
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
