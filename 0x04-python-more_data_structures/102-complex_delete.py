#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    flag = True
    if value:
        while flag:
            for key in a_dictionary:
                if a_dictionary[key] == value:
                    a_dictionary.pop(key)
                break
            flag = False
    return a_dictionary
