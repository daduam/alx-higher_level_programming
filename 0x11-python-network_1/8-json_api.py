#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
import sys

if __name__ == "__main__":
    try:
        url = "http://0.0.0.0:5000/search_user"
        query = sys.argv[1] if len(sys.argv) > 1 else ""
        r = requests.post(url, data={"q": query})
        body = r.json()
        if body:
            print("[{}] {}".format(body.get("id"), body.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
