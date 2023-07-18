#!/usr/bin/python3
# File: base.py
# Author: Oluwatobiloba Light
"""This module defines a “base” of all other classes in this project"""
import json
import csv
import turtle


class Base():
    """
    Represents the base for all the other classes in this project

    Attr:
        __nb_objects (int): Number of instantiated classes
        id (int, optional): ID of the class. Defaults to None

    Methods:
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the class

        Args:
            id (int, optional): ID of the class. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): List of dictionaries

        Returns:
            json: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if (type(list_dictionaries) != list or not
                all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by the JSON string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by the JSON string.

        This static method takes a JSON string representation of a list of
        dictionaries and returns the corresponding list. If the json_string
        is None or empty, an empty list is returned. Otherwise,
        the JSON string is converted to a list and returned.
        """
        if json_string is None or len(json_string) == 0 or json_string == '':
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates and returns an instance with all attributes already set based
        on the provided dictionary.

        Args:
            **dictionary: Double pointer to a dictionary containing
            attribute-value pairs.

        Returns:
            Base: An instance of the class with attributes set according
            to the dictionary.

        This class method takes a dictionary as a double pointer and returns
        an instance of the class with attributes set based on the key-value
        pairs in the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base.

        This class method takes a list of instances that inherit from Base
        and saves the JSON string representation of the list to a file.
        The filename is derived from the name of the class. If list_objs is
        None, an empty list is saved. The file is overwritten if it already
        exists.
        """
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8")\
                as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(Base.to_json_string(
                    [ob.to_dictionary() for ob in list_objs]))

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances created from a JSON file.

        Returns:
            list: A list of instances created from the JSON file.

        This class method loads data from a JSON file and returns a list of
        instances created from that data. The filename is derived from the
        class name, such as 'Rectangle.json' for the `Rectangle` class.
        If the file doesn't exist, an empty list is returned. Otherwise,
        the file is read, and the JSON data is loaded into a list
        of dictionaries. Each dictionary represents the attributes
        of an instance.
        """
        try:
            with open("{}.json".format(cls.__name__), 'r', encoding="utf-8")\
                    as file:
                json_file = file.read()
                return [cls.create(**item) for item in
                        Base.from_json_string(json_file)]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        with open("{}.csv".format(cls.__name__), 'w', newline="") as csvfile:
            if list_objs is None:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                for o in list_objs:
                    csv.DictWriter(csvfile, fieldnames).writerow(
                        o.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open("{}.csv".format(cls.__name__), "r", newline="")\
                    as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                list_dicts = csv.DictReader(csvfile, fieldnames)
                l_dicts = []
                for l_dict in list_dicts:
                    new_dict = {}
                    for k, v in l_dict.items():
                        new_dict[k] = int(v)
                    l_dicts.append(new_dict)
                return [cls.create(**d) for d in l_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        turt = turtle.Turtle()
        turt.screen.bgcolor("wheat")
        turt.pensize(4)
        turt.shape("circle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("black")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
