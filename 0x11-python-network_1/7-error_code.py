#!/usr/bin/python3
# File: 7-error_code.py
# Author: Oluwatobiloba Light
"""
Sends a request to the URL and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        response = requests.get(sys.argv[1])
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)