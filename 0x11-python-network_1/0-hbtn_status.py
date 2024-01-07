#!/usr/bin/python3
"""Write a Python script that
    fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as page:
        pageContent = page.read()
        print("Body response:")
        print("\t- type: {}".format(type(pageContent)))
        print("\t- content: {}".format(pageContent))
        print("\t- utf8 content: {}".format(pageContent.decode("UTF-8")))
