#!/usr/bin/python3
""" Python script that takes in a letter
    and sends a POST request to
    http://0.0.0.0:5000/search_user
    with the letter as a parameter."""


import sys
import requests
if __name__ == '__main__':
    if sys.argv[1] == 0:
        values = {'q': ""}
    else:
        values = {'q': sys.argv[1]}
    req = requests.post("http://0.0.0.0:5000/search_user", values)
    try:
        response = req.json()
        if(response != {}):
            print("{} {}".format(response.get("id"), respnse.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
