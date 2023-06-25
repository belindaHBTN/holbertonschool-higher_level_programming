#!/usr/bin/python3
"""
    This module contains a function that convert obj to JSON format
"""
import json


def to_json_string(my_obj):
    """ Function that convert obj to JSON format

    Args:
        my_obj: the obj that need to be converted

    Returns:
        JSON format object
    """
    return json.dumps(my_obj)
