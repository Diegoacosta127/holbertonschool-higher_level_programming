#!/usr/bin/python3
"""module doc"""


def write_file(filename="", text=""):
    """write file doc"""
    with open(filename, 'w+', encoding='utf8') as f:
        return f.write(text)
