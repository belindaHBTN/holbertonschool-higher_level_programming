#!/usr/bin/python3
"""
    This module contains a function that writes an Object to a text file,
    using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function that write an Object to a text file using JSON

    Args:
       my_obj: the object that need to be wrote to the file
       filename: filename
    """
    my_str = json.dumps(my_obj)
    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(my_str)
