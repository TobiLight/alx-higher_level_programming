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

    if os.path.exists('add_item.json'):
        # Load existing data from the file
        data = load_from_json_file('add_item.json')
    else:
        data = []

    # Add the arguments to the list
    data.extend(sys.argv[1:])

    # Save the updated list to the add_item.json file
    save_to_json_file(data, 'add_item.json')
