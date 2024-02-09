#!/usr/bin/python3
"""Square module."""


class Square:
    """define a square."""
    def __init__(self, size=0):
        """constructor

        Args:
            size: square side length

        Raises:
           TypeError: if size is not int
           ValueError: if zise is negative
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
