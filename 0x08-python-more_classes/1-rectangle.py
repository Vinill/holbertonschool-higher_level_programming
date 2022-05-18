#!/usr/bin/python3
"""Class Square"""


class Rectangle:

    """class Square that defines a square by 4"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.width)

    @property.setter
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif position < 0:
            raise ValueError("size must be >= 0")
        self.siz = value

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if self.size == 0:
            print("")
        for i in range(self.size):
            for j in range(self.__size):
                print("#", end="")
            print("")
