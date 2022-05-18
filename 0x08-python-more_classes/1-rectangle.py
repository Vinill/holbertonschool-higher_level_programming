#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """CLass"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """CLass"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """CLass"""
        if not isinstance(value, int):
            raise TypeError("width must be an integerr")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """CLass"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """CLass"""
        if not isinstance(value, int):
            raise TypeError("height must be an integerr")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
