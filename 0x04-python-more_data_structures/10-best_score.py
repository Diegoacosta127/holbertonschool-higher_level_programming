#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    if not a_dictionary:
        return None
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value > a:
            a = value
    return key_list[val_list.index(a)]
