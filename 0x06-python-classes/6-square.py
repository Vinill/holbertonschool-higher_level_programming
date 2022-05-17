#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            position = self.position
            if position[1] > 0:
                for x in range(position[1]):
                    print("")
            for x in range(self.size):
                print(" " * position[0] + "#" * self.size)

    #  for i in range(self.size):
    #    for j in range(self.__size):
    #         print("#", end="")
    #    print("")