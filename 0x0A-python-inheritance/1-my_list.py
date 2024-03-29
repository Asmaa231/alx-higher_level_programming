#!/usr/bin/python3
"""Module Mylist class"""


class Mylist(list):
    """Custom Mylist class"""
    def print_sorted(self):
        """Method for printed sorted list"""
        print(sorted(self))
