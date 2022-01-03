#!/usr/bin/python3
def no_c(my_string):
    a = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            a = a + c
    return a
