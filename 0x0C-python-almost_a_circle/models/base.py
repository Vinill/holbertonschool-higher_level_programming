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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Def to_json_string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ def save to file """
        if list_objs is None:
            with open(cls.__name__+".json", "w") as f:
                f.write(cls.to_json_string(None))
        else:
            with open(cls.__name__+".json", "w") as f:
                f.write(cls.to_json_string([obj.to_dictionary()
                                            for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Def to_json_string"""
        if json_string is None or json_string == "":
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
