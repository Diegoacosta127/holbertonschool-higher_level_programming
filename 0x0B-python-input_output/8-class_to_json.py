#!/usr/bin/python3
"""module doc"""
import json


def class_to_json(obj):
    """class_to_json doc"""
    return json.dumps(obj.__dict__)
