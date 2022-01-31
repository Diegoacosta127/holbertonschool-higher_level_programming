#!/usr/bin/python3
"""module doc"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square doc"""
    def __init__(self, size):
        """constructor doc"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area doc"""
        return self.__size ** 2

    def __str__(self):
        """str doc"""
        return(f"[Rectangle] {self.__size}/{self.__size}")
