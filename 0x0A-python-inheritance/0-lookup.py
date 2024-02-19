#!/usr/bin/python3
"""Module for lookup method"""


def lookup(obj):
    """look up obj attributes and methods of an object
    Args:
        obj: object to list
    Returns:
        list: list of attribute
    """
    return dir(obj)
