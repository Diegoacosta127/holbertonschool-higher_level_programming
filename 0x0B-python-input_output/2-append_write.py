#!/usr/bin/python3
"""module doc"""


def append_write(filename="", text=""):
    """append_write doc"""
    with open(filename, 'a+', encoding='utf8') as f:
        return f.write(text)
