#!/usr/bin/python3
"""module doc"""


def pascal_triangle(n):
    """pascal_triangle doc"""
    re = []
    pre_aux = []
    for i in range(n):
        aux = []
        pos1 = -1
        pos2 = 0
        for j in range(len(pre_aux) + 1):
            if pos1 == -1 or pos2 == len(pre_aux):
                aux += [1]
            else:
                aux += [pre_aux[pos1] + pre_aux[pos2]]
            pos1 += 1
            pos2 += 1
        re.append(aux)
        pre_aux = aux[:]
    return re
