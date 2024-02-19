#!/usr/bin/python3
"""Module for rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """A subclass representing square"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """methode return square area"""
        return self.__size ** 2
