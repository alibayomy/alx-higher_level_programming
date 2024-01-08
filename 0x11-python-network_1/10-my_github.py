#!/usr/bin/python3
""" a Python script that takes your GitHub
    credentials(username and password)
    and uses the GitHub API to display your id"""


import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    myAuth = HTTPBasicAuth(username, password)
    myReq = requests.get("https://api.github.com/user", auth=myAuth)
    print(myReq.json().get("id"))
