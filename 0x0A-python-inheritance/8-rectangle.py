#!/usr/bin/python3

class BaseGeometry:
    """My class BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """My class Rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__heigth = height
