#!/usr/bin/python3
"""Square module."""


class Square:
    """define a square."""
    def __init__(self, size=0):
        """constructor

        Args:
            size: square side length
        """
        self.size = size

    @property
    def size(self):
        """Property for square side length

        Raises:
           TypeError: if size is not int
           ValueError: if zise is negative
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area of square

        Return: Square area
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with #"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()
