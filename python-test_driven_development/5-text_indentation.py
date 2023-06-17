#!/usr/bin/python3

"""
This module provides a function that prints text in special format.
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters .?:

    Arg:
    text: the text that need to be modified

    Return:
    No return.

    Raises:
    TypeError: If the argument is not an string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n").replace("?", "?\n").replace(":", ":\n")
    words = text.split("\n")
    result = "\n\n".join(map(lambda x: x.strip(), words))
    print(result, end="")
