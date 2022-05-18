#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:

    """CLass"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """CLass"""

    @property
    def width(self):
        return(self.__width)

    """CLass"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integerr")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """CLass"""

    @property
    def height(self):
        return(self.__height)

    """CLass"""

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integerr")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """CLass"""
