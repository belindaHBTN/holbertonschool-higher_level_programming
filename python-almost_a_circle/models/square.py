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
