#!/usr/bin/python3
# File:11-student.py
# Author: Oluwatobiloba Light
"""Defines a class Student."""


class Student:
    """
    Represents a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Gets a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs
                    if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The k/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)

if __name__ == "__main__":
    import sys
    import os
    read_file = __import__('0-read_file').read_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name,
          student_1.last_name, student_1.age))

    save_to_json_file(j_student_1, path)
    read_file(path)
    print("\nSaved to disk")

    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name,
          new_student_1.last_name, new_student_1.age))

    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file(path)

    new_student_1.reload_from_json(j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name,
          new_student_1.last_name, new_student_1.age))
