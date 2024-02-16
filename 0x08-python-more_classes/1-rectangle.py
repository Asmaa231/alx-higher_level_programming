#!/usr/bin/python3
"""Define an empty class rectangle"""


class Rectangle:
    """Empty representation of a rectangle"""
    def __init__(self, width=0, height=0):
	"""Initialize the rectangle"""
	self.width = width
	self.height = height
	
    @property
    def width(self):
	"""getter for private attribute width """
	return self.__width
		
    @width.setter
    def width(self, value):
	"""getter for private attribute width """
	if type(value) in not int:
		raise TypeError("width must be integer")
	if value < 0:
                raise ValueError("width must be >= 0")
	self.__width = value
		
    @property
    def height(self):
	"""getter for private attribute height """
	return self.height
		
    @height.setter
    def height(self, value):
	"""getter for private attribute height """
	if type(value) in not int:
		raise TypeError("height must be integer")
	if value < 0:
		raise ValueError("height must be >= 0")
	self.__height = value
