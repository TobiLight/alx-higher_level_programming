#!/usr/bin/python3
#File: 10-my_github.py
#Author: Oluwatobiloba Light
"""
Uses the GitHub API to display your id.
"""
import requests
import requests.auth
import sys


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    print(response.json().get("id"))