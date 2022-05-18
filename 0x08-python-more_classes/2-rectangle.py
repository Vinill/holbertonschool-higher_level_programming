#!/usr/bin/python3
"""Class Rectangle"""


from turtle import width


class Rectangle:

    """Class Rectangle that defines a rectangle by"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integerr")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integerr")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return((self.height * 2) + (self.width * 2))