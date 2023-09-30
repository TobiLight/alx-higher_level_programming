#!/usr/bin/python3
# File: 6-post_email.py
# Author: Oluwatobiloba Light
"""
Sends a POST request a URL with email as a parameter and displays the body of
the response.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        response = requests.get(sys.argv[1], {"email: {}".format(sys.argv[2])})
        print(response.text)
