#!/usr/bin/python3
"""
    This module contains a function that return an obj represented by JSON
"""
import json


def from_json_string(my_str):
    """ Function that convert JSON format to an object

    Args:
        my_str: the JSON string that need to be converted

    Returns:
        Python data structure object
    """
    return json.loads(my_str)
