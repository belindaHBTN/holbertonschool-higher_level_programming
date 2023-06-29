#!/usr/bin/python3

"""
    This is a module contain a Base class
"""
import json


class Base:
    """
        This is a Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize an instance of class Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            return the JSON string  representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Save a list of objects into a file
        """
        file_name = "{}.json".format(cls.__name__)
        list_dict = []

        if not list_objs:
            pass
        else:
            for list_obj in list_objs:
                list_dict.append(list_obj.to_dictionary())
        list_str = cls.to_json_string(list_dict)

        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(list_str)
