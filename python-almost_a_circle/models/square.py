#!/usr/bin/python3

"""
    This module presents a square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        This is a class repsents a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes an instance of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            print out specific content
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
            size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            size setter
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            assign an argument to each attribute
        """
        if len(args) != 0:
            keys = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
