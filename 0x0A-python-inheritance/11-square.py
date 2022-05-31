#!/usr/bin/python3
"""Import 9"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """My class Square"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' Overrides the area method, and returns the area '''
        return(self.__size * self.__size)

    def __str__(self):
        ''' Prints the dimensions of the square '''
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))
