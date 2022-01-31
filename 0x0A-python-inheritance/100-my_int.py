#!/usr/bin/python3
"""module doc"""


class MyInt(int):
    """class MyInt doc"""
    def __eq__(self, other):
        """eq doc"""
        return False

    def __ne__(self, other):
        """ne doc"""
        return True
