#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    a = -999999999
    for i in my_list:
        if i > a:
            a = i
    return a
