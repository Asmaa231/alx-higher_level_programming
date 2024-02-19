#!/usr/bin/python3
"""Module mylist class"""


class Mylist(list):
    """Custom mylist class"""
    def print_sorted(self):
        """Method for printed sorted list"""
        print(sorted(self))
