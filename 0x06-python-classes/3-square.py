#!/usr/bin/python3
"""Empty class"""


class Square:

    """class Square that defines a square by 2"""

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return(self.__size * self.__size)
