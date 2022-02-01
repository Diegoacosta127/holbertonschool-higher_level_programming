#!/usr/bin/python3
"""module doc"""


def read_file(filename=""):
    """read_file doc"""
    with open(filename, encoding='utf8') as f:
        print(f.read(), end="")
