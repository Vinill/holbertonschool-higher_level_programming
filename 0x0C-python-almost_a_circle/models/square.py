#!/usr/bin/python3
""" class Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ def str """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def update(self, *args, **kwargs):
        """Definition Update"""
        list_args = ["id", "size", "x", "y"]
        if args:
            count = 0
            for i in args:
                setattr(self, list_args[count], i)
                count += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
