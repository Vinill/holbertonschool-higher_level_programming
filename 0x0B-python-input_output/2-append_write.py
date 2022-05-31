#!/usr/bin/python3
"""
function that appends a string at the end of a text file
(UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """append write"""
    with open(filename, mode="a", encoding="UTF-8") as file:
        return(file.write(text))
