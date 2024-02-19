#!/usr/bin/python3
"""Modul Mylist class"""


class Mylist(list):
    """Custom mylist class"""
    def print_sorted(self):
        """Method for printed sorted list"""
        print(sorted(self))
