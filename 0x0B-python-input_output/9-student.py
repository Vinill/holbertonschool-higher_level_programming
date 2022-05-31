#!/usr/bin/python3
"""
class Student that defines a student by
"""


class Student():
    """Def class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            dict1 = {}
            
            return(vars(self))
