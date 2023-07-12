#!/usr/bin/python3
# File: 7-add_item.py
# Author: Oluwatobiloba Light
"""Add all arguments to a Python list and save them to a file."""
import sys
import os

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = 'add_item.json'
    args = len(sys.argv)

    if not os.path.isfile(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('[]')

    if args > 1:
        data = load_from_json_file(filename)
        for i in range(1, args):
            data.append(sys.argv[i])
        save_to_json_file(data, filename)
