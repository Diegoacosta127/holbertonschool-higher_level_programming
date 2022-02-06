#!/usr/bin/python3
"""module doc"""
import json


class Base:
    """Base class doc"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor doc"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file doc"""
        new_list = []
        name = str(cls.__name__) + ".json"
        with open(name, 'w', encoding='utf8') as f:
            if list_objs is None:
                f.write(cls.to_json_string(new_list))
            else:
                for obj in list_objs:
                    new_list.append(cls.to_dictionary(obj))
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string doc"""
        if type(json_string) is not str:
            raise TypeError("json_string must be a string")
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create doc"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        if dummy:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load_from_file doc"""
        l_instances = []
        with open(f"{cls.__name__}.json", 'r') as f:
            for line in f:
                try:
                    instances = cls.from_json_string(line)
                    for item in instances:
                        l_instances.append(cls.create(**item))
                except Exception as ex:
                    print(f"Exception!\n{ex}")
        return l_instances
