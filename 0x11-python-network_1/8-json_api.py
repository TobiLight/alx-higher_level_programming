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
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})
    try:
        resp = response.json()
        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"),
                                   resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
