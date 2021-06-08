#!/usr/bin/python3
"""
Contains definition of the class Base
"""
import json
import os.path
import csv


class Base:
    """Base class - base class of all classes in this project
                  - manage id attribute in all future classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance of class Base

        Args:
            id (int): id value for id attribute
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        to_save = []
        if list_objs is None:
            with open(filename, mode="w", encoding="UTF-8") as f:
                f.write(to_save)
        else:
            for obj in list_objs:
                to_save.append(obj.to_dictionary())
            with open(filename, mode="w", encoding="UTF-8") as f:
                f.write(cls.to_json_string(to_save))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list representation of a JSON string representation

        Args:
            json_string (JSON string): string to be decoded to a python list
        """
        if json_string is None or len(json_string) == 0:
            res = []
            return res
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instance with all attributes already set

        Args:
            dictionary (pointer): "double pointer" to a dictionary containing
                                  keyword:value pairs
        """
        temp = cls(1, 1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """Returns a list of class instances created from json file contents"""
        filename = str(cls.__name__) + ".json"
        res = []
        if os.path.isfile(filename):
            with open(filename, encoding="UTF-8") as f:
                data = f.read()
            data = data.strip("]")
            data = data.strip("[")
            s, e = 0, 0
            res = []
            while 1:
                s = data.find("{", e)
                e = data.find("}", s)
                if s == -1 or e == -1:
                    return res
                curr = data[s:e+1]
                l = cls.from_json_string(curr)
                temp = cls.create(**l)
                res.append(temp)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write csv representation of python list_objs to file"""
        if list_objs is None:
            filename = str(type(self).__name__) + ".json"
            with open(filename, mode="w", encoding="UTF-8") as f:
                f.write("[]")
        else:
            filename = str(type(list_objs[0]).__name__) + ".csv"
            with open(filename, mode="w", encoding="UTF-8") as f:
                writer = csv.writer(f)
                for obj in list_objs:
                    if str(cls.__name__) == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
                    elif str(cls.__name__) == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of class instances created from csv file contents"""
        filename = str(cls.__name__) + ".csv"
        res = []
        if os.path.isfile(filename):
            with open(filename, encoding="UTF-8") as f:

                if str(cls.__name__) == "Rectangle":
                    reader = csv.DictReader(f, fieldnames=['id', 'width',
                                                           'height', 'x', 'y'])
                elif str(cls.__name__) == "Square":
                    reader = csv.DictReader(f, fieldnames=['id', 'size',
                                                           'x', 'y'])
                for row in reader:
                    row = {x: int(y) for x, y in row.items()}
                    temp = cls.create(**row)
                    res.append(temp)
                return res
