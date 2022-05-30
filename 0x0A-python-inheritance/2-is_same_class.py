#!/usr/bin/python3
"""function that returns True if the object is exactly 
an instance of the specified class otherwise False."""


def is_same_class(obj, a_class):
    """My class"""
    if type(obj) in a_class:
        return True
    return False
