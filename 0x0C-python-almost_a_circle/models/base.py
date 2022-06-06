#!/usr/bin/python3
""" This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs) """

import json

class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ def init """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    def to_json_string(list_dictionaries):
        """Def to_json_string"""
        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
