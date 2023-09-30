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
        val = {"email: {}".format(sys.argv[2])}
        response = requests.post(sys.argv[1], data=val)
        print(response.text)
