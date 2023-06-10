#!/usr/bin/python3
# File: 2-args.py
# Author: Oluwatobiloba Light
if __name__ == "__main__":
    """Prints the number of and the list of its arguments."""
    from sys import argv

    if len(argv) < 2:
        print("0 arguments.")
    elif len(argv) >= 2:
        print("{}: {}".format(1 if len(argv) == 2 else len(argv) - 1,
                              "argument" if len(argv) == 2 else "arguments"))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
