#!/usr/bin/python3
"""module task 10"""


class Student:
    """representation of a Student"""
    def __init__(self, first_name, last_name, age):
        """initalize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dic representation of student,
        If attrs is a list of strings,
        only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict_.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
