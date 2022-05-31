#!/usr/bin/python3
''' Module inherits_from '''


def inherits_from(obj, a_class):
    """My class inherits_from"""
    return (issubclass(type(obj), a_class) and a_class is not type(obj))
