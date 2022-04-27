#!/usr/bin/python3
def islower(c):
    letter = ord(c)
    for low in range(97, 122):
        if low == letter:
            return True
    return False
