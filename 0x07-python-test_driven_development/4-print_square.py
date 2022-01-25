#!/usr/bin/python3
"""module doc"""


def print_square(size):
    """print_square doc"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(0, size):
            for col in range(0, size):
                print("#", end="")
            print()
