#!/usr/bin/python3
"""Module for rectangle class"""
BaseGeometry = __import__('9-rectangle').Rectangle


class Square(BaseGeometry):
    """A subclass representing square"""
    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """methode return square area"""
        return self.__size ** 2
