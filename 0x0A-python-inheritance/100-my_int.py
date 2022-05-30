#!/usr/bin/python3


class MyInt(int):

    """My class MyInt"""

    def __init__(self, result):
        self.resultado = result

    def __eq__(self, value):
        return False

    def __ne__(self, value):
        return True
