#!/usr/bin/python3
""" Python script that takes in a letter
    and sends a POST request to
    http://0.0.0.0:5000/search_user
    with the letter as a parameter."""


import sys
import requests


if __name__ == "__main__":
    myLetter = "" if len(sys.argv) == 1 else sys.argv[1]
    subD = {"q": myLetter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=subD)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
