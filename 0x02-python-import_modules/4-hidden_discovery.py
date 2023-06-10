#!/usr/bin/python3
# File: 4-hidden_discovery.py
# Author: Oluwatobiloba Light

if __name__ == "__main__":
    """Print all the names defined by the compiled
       module hidden_4.pyc"""
    import hidden_4
    names = dir(hidden_4)
    for i in range(len(names)):
        if "__" not in names[i]:
            print("{}".format(names[i]))
