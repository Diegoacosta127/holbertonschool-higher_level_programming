#!/usr/bin/python3
"""module doc"""


def text_indentation(text):
    """indents a text by tokens"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        string = ""
        for char in text:
            if char in ['.', '?', ':']:
                string += char
                print(string.strip())
                print()
                string = ""
            else:
                string += char
        print(string.strip(), end="")
