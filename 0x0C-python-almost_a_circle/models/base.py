#!/usr/bin/python3
"""my Base class definition"""
import json


class Base:
    """My own definition of Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        mylst = []
        if list_objs is not None:
            for obj in list_objs:
                mylst = mylst + [obj.to_dictionary()]

        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(mylst))

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy_rec = cls(1, 1, 1, 1)
            dummy_rec.update(**dictionary)

        elif cls is Square:
            dummy_rec = cls(1, 1, 1)
            dummy_rec.update(**dictionary)
        return dummy_rec

    @classmethod
    def load_from_file(cls):
        with open("{}.json".format(cls.__name__), "r", encoding="utf-8") as f:
            if f is None:
                return []
            else:
                jsn_str = f.read()
                mylst = cls.from_json_string(jsn_str)
                return [cls.create(**obj) for obj in mylst]
