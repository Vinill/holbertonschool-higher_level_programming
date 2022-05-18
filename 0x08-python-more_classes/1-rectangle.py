#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:

    """"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.width)

    @property.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integerr")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.siz = value

    @property.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integerr")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.siz = value

    def height(self):
        return(self.height * self.width)

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(self.size):
            for j in range(self.__size):
                print("#", end="")
            print("")
