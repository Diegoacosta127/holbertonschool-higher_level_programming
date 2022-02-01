#!/usr/bin/python3
"""module doc"""


class Student:
    """class Student doc"""
    def __init__(self, first_name, last_name, age):
        """constructor doc"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict repr of a Student instance"""
        ret = {}
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return self.i__dict__
            for key in set(self.__dict__.keys()) & set(attrs):
                ret.setdefault(key, self.__dict__.get(key))
            return ret
        return self.__dict__

    def reload_from_json(self, json):
        """reload_from_json doc"""
        for item in dict(self.__dict__):
            if item in json:
                self.__dict__[item] = json[item]
