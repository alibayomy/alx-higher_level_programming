#!/usr/bin/python3
"""a python script to solve
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)"""


import sys
import requests

if __name__ == '__main__':
    repoName = sys.argv[1]
    ownerName = sys.argv[2]
    host = "https://api.github.com/repos/"
    url = host + ownerName + '/' + repoName + '/commits'
    r = requests.get(url)
    commits = r.json()
    for i in range(10):
        print("{}: {}".format(commits[i].get("sha"),
                              commits[i].get("commit").get("author").get("name")))
