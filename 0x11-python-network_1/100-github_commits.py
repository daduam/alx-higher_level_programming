#!/usr/bin/python3
"""
Evaluates candidates applying for a back-end position with
multiple technical challenges
"""


import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    last_ten_commits = r.json()[:10]
    for commit in last_ten_commits:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
