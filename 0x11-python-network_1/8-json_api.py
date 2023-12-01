#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
"""
import sys
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    r = requests.post(url, data={'q': letter})
    try:
        data = r.json()
        if len(data) == 0:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except ValueError:
        print("Not a valid JSON")
