#!/usr/bin/python3
# File: 5-hbtn_header.py
# Author: Oluwatobiloba Light
"""
Sends a request to the URL and displays the value of the variable X-Request-Id
in the response header
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        response = requests.get(sys.argv[1])
        if 'X-Request-Id' in response.headers:
            print("{}".format(response.headers['X-Request-Id']))
