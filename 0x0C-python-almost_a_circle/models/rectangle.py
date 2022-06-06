#!/usr/bin/python3
""" Write the class Rectangle that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ class rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ def init """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """ property height """
        return self.__height

    @height.setter
    def height(self, value):
        """ def height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """ property width """
        return self.__width

    @width.setter
    def width(self, value):
        """ def width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """ property x """
        return self.__x

    @x.setter
    def x(self, value):
        """ def x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ property y """
        return self.__y

    @y.setter
    def y(self, value):
        """ def y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ def area """
        return self.__width * self.__height

    def display(self):
        """ def display """
        print(f"\n" * self.__y, end="")
        for i in range(self.__height):
            print(f" " * self.__x, end="")
            print(f"#" * self.__width)

    def __str__(self):
        """ def str """
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Definition Update"""
        list_args = ["id", "width", "height", "x", "y"]
        if args:
            count = 0
            for i in args:
                setattr(self, list_args[count], i)
                count += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Def to_dictionary"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
