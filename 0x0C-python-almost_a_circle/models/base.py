#!/usr/bin/python3
"""Module for base class"""


Class Base:
    """Representation for oop heirarchy base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects
