#!/usr/bin/python3
"""module doc"""


def say_my_name(first_name, last_name=""):
    """say_my_name doc"""
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        else:
            raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
    return
