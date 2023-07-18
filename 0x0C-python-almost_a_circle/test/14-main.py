#!/usr/bin/python3
""" 14-main """
import sys
import os

# Append the path to the models directory
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))