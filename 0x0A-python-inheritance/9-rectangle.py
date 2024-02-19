#!/usr/bin/python3
"""Module for rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass representing Rectangle"""
    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """methode return area"""
        return self.__width * self.__height

    def __str__(self):
        """string representing method"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
