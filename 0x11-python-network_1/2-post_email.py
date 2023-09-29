#!/usr/bin/python3
# File: 2-post_email.py
# Author: Oluwatobiloba Light
"""
Sends a POST request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        val = {"email": sys.argv[2]}
        data = urllib.parse.urlencode(val)
        data = data.encode('ascii')
        req = urllib.request.Request(sys.argv[1], data)
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
