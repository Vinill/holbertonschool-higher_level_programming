#!/usr/bin/python3
"""
Function that writes a string to a text file
(UTF8) and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, mode="w", encoding="UTF-8") as file:
        return(file.write(text))
