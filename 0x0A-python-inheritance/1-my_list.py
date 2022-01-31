#!/usr/bin/python3
"""module doc"""


class MyList(list):
    """class doc"""
    def print_sorted(self):
        """print_sorted doc"""
        for item in self:
            if type(item) is not int:
                raise TypeError("must be a list of integers")
        print(sorted(self))
