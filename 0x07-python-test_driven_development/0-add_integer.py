#!/usr/bin/python3
"""module: 0-add_integer"""


def add_integer(a, b=98):
    """
    TypeError: b must be an integer
    """
    if type(a) is not int or not a:
        if type(a) is not float or not a:
            raise TypeError("a must be an integer")
        else:
            a = int(a)
    if type(b) is not int:
        if type(b) is not float:
            raise TypeError("b must be an integer")
        else:
            b = int(b)
    return a + b
