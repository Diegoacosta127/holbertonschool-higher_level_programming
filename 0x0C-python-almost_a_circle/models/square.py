#!/usr/bin/python3
"""module doc"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class doc"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor doc"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str doc"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {super().width}"

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update doc"""
        attr = {0: "id", 1: "size", 2: "x", 3: "y"}
        if args:
            if len(args) < 5:
                for i in range(len(args)):
                    setattr(self, attr[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """to_dictionary doc"""
        my_dict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return my_dict
