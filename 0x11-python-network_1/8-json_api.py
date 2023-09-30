#!/usr/bin/python3
# File: 8-json_api.py
# Author: Oluwatobiloba Light
"""
Sends a POST request to http://0.0.0.0:5000/search_user with the letter as a
parameter.
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) > 1:
        response = requests.get("http://0.0.0.0:5000/search_user",
                                params=sys.argv[1])
        if 'application/json' in response.headers['Content-Type']:
            print("[{}] {}".format(response.json()
                  ['id'], response.json()['name']))
    else:
        response = requests.get("http://0.0.0.0:5000/search_user", params="")
        if 'application/json' in response.headers['Content-Type']:
            print(response.json())
