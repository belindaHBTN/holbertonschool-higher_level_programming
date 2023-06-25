#!/usr/bin/python3
"""
    This module contains a function that write text to a file
"""


def write_file(filename="", text=""):
    """ Function that write text a file

    Args:
        filename: optional arg, filename
        text: optional arg, text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return len(text)
