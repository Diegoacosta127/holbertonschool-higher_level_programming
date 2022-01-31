#!/usr/bin/python3
"""module doc"""


def inherits_from(obj, a_class):
    """method doc"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
