#!/usr/bin/python3
"""contain class Myint"""



class MyInt(int):
    """rebel version of int"""
    def __new__(cls, *args, **kwargs):
        """creats new instance for the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def__eq__(self, other):
        """what was != is == now"""
        return int(self) != other

    def__ne__(self, other):
        """what was == is != now"""
        return int(self) == other
