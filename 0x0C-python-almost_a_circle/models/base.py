#!/usr/bin/python3
"""Module for base class"""
from json import dumps, loads


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """josnifiy a dictionary"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save josnified odj to file"""
        if list_objs is not None:
            list_objs = [o.dictionary() for o in list_objs]
        with open("().join".format(cls.__name_), "w", encoding="utf-8") as f:
            f.write(cls.to_join_string(lists_objs))
