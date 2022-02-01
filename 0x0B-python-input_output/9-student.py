#!/usr/bin/python3
"""module doc"""


class Student:
    """class Student doc"""
    def __init__(self, first_name, last_name, age):
        """constructor doc"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict repr of a Student instance"""
        return self.__dict__
