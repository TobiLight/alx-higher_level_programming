#!/usr/bin/python3
# File: 3-error_code.py
# Author: Oluwatobiloba Light
"""
Sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        req = Request('{}'.format(sys.argv[1]))
        try:
            with urlopen(req) as response:
                print("{}".format(response.read().decode('utf-8')))
        except HTTPError as e:
            print("Error code: {}", e.code)
