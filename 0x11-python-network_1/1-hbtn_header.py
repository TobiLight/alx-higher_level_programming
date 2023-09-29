#!/usr/bin/python3
# File: 1-hbtn_header.py
# Author: Oluwatobiloba Light
"""
Snds a request to the URL and displays the value of the X-Request-Id variable
found in the header of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request('{}'.format(sys.argv[1]))
    with urllib.request.urlopen(req) as response:
        if 'X-Request-Id' in response.headers:
            