#!/usr/bin/python3
"""module doc"""


class BaseGeometry:
    """class BaseGeometry doc"""
    def area(self):
        """area doc"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """integer_validator doc"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """class Rectangle doc"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
