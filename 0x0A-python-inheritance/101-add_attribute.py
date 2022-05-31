#!/usr/bin/python3
''' Module to add attribute to a class '''


def add_attribute(obj, atr, value):
    ''' Adds an attribute to a class '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, atr, value)
