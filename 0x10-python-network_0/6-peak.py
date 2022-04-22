#!/usr/bin/bash
"""Find a peak of a list of numbers"""


def find_peak(list_of_integers):
    """Find a peak of a list of numbers"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
