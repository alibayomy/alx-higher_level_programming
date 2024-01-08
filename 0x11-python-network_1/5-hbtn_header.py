#!/usr/bin/python3
"""a Python script that takes in a URL,
    sends a request to the URL and displays
    the value of the variable X-Request-Id
    in the response header"""


if __name__ == '__main__':
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status")
    headers = r.headers
    print(headers['X-Request-Id'])
