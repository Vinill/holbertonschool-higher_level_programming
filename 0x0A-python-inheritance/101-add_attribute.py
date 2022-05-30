#!/usr/bin/python3

def add_attribute(obj, atr, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, atr, value)
