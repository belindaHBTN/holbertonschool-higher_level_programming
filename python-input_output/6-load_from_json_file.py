#!/usr/bin/python3
"""
    This module contains a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file”

    Args:
       filename: filename

    Return:
        an object
    """
    with open(filename, mode="r", encoding="utf-8") as my_file:
        return json.load(my_file)
