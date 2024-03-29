#!/usr/bin/python3
# File: 3-error_code.py
# Author: Oluwatobiloba Light
"""
Sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        req = urllib.request.Request(sys.argv[1])
        try:
            with urllib.request.urlopen(req) as response:
                print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
