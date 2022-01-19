#!/usr/bin/python3
"""10. ByteCode -> Python #5"""
import math


class MagicClass:
    """Class: MagicClass"""
    def __init__(self, radius=0):
        """constructor method"""
        self.radius = 0
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        self.__radius = radius
        return None

    def area(self):
        """calculates area of a circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """calculates the circumference"""
        return (2 * math.pi) * self.__radius
