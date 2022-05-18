#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:

    """Class Rectangle that defines a rectangle by"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integerr")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @property
    def height(self):
        return(self.height)
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integerr")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.height = value

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return((self.height * 2) + (self.width * 2))