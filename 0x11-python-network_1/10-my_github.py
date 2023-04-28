#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


import requests
import requests.auth
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    auth = requests.auth.HTTPBasicAuth(username, token)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
