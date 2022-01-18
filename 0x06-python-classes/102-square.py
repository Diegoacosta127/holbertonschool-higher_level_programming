#!/usr/bin/python3
"""i. Access and update private attribute"""


class Square:
    """Class: Square"""
    def __init__(self, size=0):
        """constructor method"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """int: getter"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int or type(size) is not float:
            raise TypeError("size must be an number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of a square"""
        return self.__size ** 2

    def __eq__(self, other):
        """equal"""
        return self.__size == other

    def __lt__(self, other):
        """lower than"""
        return self.__size < other

    def __le__(self, other):
        """lower or equal than"""
        return self.__size <= other

    def __gt__(self, other):
        """greater than"""
        return self.__size > other

    def __ge__(self, other):
        """greater or equal than"""
        return self.__size >= other

    def __ne__(self, other):
        """not equal"""
        return self.__size != other
