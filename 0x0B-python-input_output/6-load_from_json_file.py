#!/usr/bin/python3
"""module doc"""
import json


def load_from_json_file(filename):
    """load_from_json_file doc"""
    with open(filename) as f:
        return (json.load(f))
