#!/usr/bin/python3
"""6. Coordinates of a square"""


class Square:
    """defines a square
    """
    def __init__(self, size=0, pos=(0, 0)):
        """constructor method

        Args:
            size (int): size of the square.
            position (int, int): position to move the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(pos, type((int, int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif pos[0] < 0 or pos[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(pos[0], int) or not isinstance(pos[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__pos = pos

    @property
    def size(self):
        """int: getter"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    @property
    def position(self):
        """(int, int): getter"""
        return self.__pos

    @position.setter
    def position(self, value):
        if not isinstance(value, type((int, int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__pos = value

    def my_print(self):
        """prints something"""
        if self.__size == 0:
            print()
        else:
            i = 0
            j = 0
            k = 0
            loop = 0
            for k in range(self.__pos[1]):
                print()
            for i in range(self.__size):
                for loop in range(self.__pos[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
