#!/usr/bin/python3
''' Module that creates a class '''


class BaseGeometry:
    """My class BaseGeometry"""

    def area(self):
        ''' Area function (not implemented) '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Validates a value '''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} be greater than 0".format(name))
