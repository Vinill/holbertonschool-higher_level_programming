#!/usr/bin/python3
''' Module that inverts eq and ne methods of int class '''


class MyInt(int):
    """My class MyInt"""

    def __eq__(self, value):
        """Equal to inverted"""
        return False

    def __ne__(self, value):
        """Not equal to inverted"""
        return True
