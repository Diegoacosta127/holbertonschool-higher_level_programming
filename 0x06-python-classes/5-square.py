#!/usr/bin/python3
"""5. Printing a square"""


class Square:
    """Class: Square"""
    def __init__(self, size=0):
        """construcor method"""
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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """calculates the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """prints a square"""
        if self.__size == 0:
            print()
        else:
            i = 0
            j = 0
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
