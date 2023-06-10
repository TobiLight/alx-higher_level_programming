#!/usr/bin/python3
# File: ./3-infinite_add.py
# Author: Oluwatobiloba Light

if __name__ == "__main__":
    """Prints the result of the addition of all arguments"""
    from sys import argv

    result = 0
    if len(argv) < 2:
        print("{}".format(0))
    else:
        for i in range(1, len(argv)):
            result += int(argv[i])
    print("{}".format(result))
