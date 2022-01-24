#!/usr/bin/python3
"""module doc"""


class Rectangle:
    """class doc"""
    def __init__(self, width=0, height=0):
        """init doc"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = height
            self.width = width

    @property
    def width(self):
        """width getter doc"""
        return self.width

    @property
    def height(self):
        """height getter doc"""
        return self.height

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """area doc"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter doc"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """str doc"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i is not self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """repr doc"""
        return (type(self).__name__ + "(" + str(self.__width) + "," +
                str(self.__height) + ")")
