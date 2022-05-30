#!/usr/bin/python3
"""Import 9"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """My class Square"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return(self.__size * self.__size)

    def __str__(self):
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
