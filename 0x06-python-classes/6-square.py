#!/usr/bin/python3
"""6. Coordinates of a square"""


class Square:
    """defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
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
        if not isinstance(position, type((int, int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        """returns the area of the square"""
        return self.__size * self.__size

    @property
    def position(self):
        """(int, int): getter"""
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, type((int, int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """prints something"""
        if self.__size == 0:
            print()
        else:
            i = 0
            j = 0
            k = 0
            loop = 0
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for loop in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
