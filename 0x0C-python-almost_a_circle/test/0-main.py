#!/usr/bin/python3
""" 0-main """
import sys
import os

# Append the path to the models directory
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from models.base import Base


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
