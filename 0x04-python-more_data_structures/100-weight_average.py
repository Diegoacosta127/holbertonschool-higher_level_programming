#!/usr/bin/python3
def weight_average(my_list=[]):
    acum = 0
    nose = 0
    if not my_list:
        return 0
    for elem in my_list:
        acum = acum + (elem[0] * elem[1])
        nose = nose + elem[1]
    return acum / nose
