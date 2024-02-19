#!/usr/bin/python3
"""Write a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, att, value):
    """adds a new attribute to an object
    Args:
        obj (any): object to add attribute
        att (str): attribute name
        value (any): attribute value

    Raises:
        TypeError: if attr can not be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
