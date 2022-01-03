#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        if len(tuple_b) == 0:
            tuple_c = (0, 0)
        elif len(tuple_b) == 1:
            tuple_c = (tuple_b[0], 0)
        else:
            tuple_c = tuple_b
    elif len(tuple_a) == 1:
        if len(tuple_b) == 0:
            tuple_c = (tuple_a[0], 0)
        elif len(tuple_b) == 1:
            tuple_c = (tuple_a[0] + tuple_b[0], 0)
        else:
            tuple_c = (tuple_a[0] + tuple_b[0], tuple_b[1])
    else:
        if len(tuple_b) == 0:
            tuple_c = tuple_a
        elif len(tuple_b) == 1:
            tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1])
        else:
            tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c
