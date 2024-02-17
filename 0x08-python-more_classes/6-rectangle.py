#!/usr/bin/python3
"""Define an empty class rectangle"""


class Rectangle:
	"""Empty representation of a rectangle"""
	
	number_of_instance = 0
	
	def __init__(self, width=0, height=0):
	"""Initialize the rectangle"""
		self.width = width
		self.height = height
		rectangle.number_of_instance += 1
	
	def __del__(self):
		"""Print message when rectangle deletion"""
		print("Bye rectangle...")
		rectangle.number_of_instance -= 1
		
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
		return self.__height
		
	@height.setter
	def height(self, value):
		"""getter for private attribute height """
		if type(value) in not int:
			raise TypeError("height must be integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

	def area(self):
		"""Return rectangle area"""
		return self.__width * self.__height
	
	def primeter(self):
		"""Return rectangle preimeter"""
		return self.__width * 2 + self.__height * 2
	
	def __str__(self):
		"""Return printable rectangle string"""
		string = " "
		if self.__width != 0 and self.__height != 0
		string += '\n'.join("#" * self.__width 
		                    for j in range(self.__height))
		return string
	
	def __repr__(self):
		"""Return printable rectangle string for developer reproduction"""
		return "Rectangle("{:d}, {:d}".format(self.__width, self.__height))"
