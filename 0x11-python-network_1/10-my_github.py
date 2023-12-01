#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    auths = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auths)
    print(r.json().get("id"))
