#!/usr/bin/python3
"""module doc"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file doc"""
    with open(filename, 'w+', encoding='utf8') as f:
        return json.dump(my_obj, f)
