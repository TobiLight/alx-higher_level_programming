#!/usr/bin/python3
""" 12-main """
import sys
import os

# Append the path to the models directory
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)
