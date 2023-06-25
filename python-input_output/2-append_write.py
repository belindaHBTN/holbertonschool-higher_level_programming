#!/usr/bin/python3
"""
    This module contains a function that append text to a file
"""


def append_write(filename="", text=""):
    """ Function that append text to a file

    Args:
        filename: optional arg, filename
        text: optional arg, text
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
