#!/usr/bin/python3
'''script that takes in a URL, sends a request to the URL
 and displays the value of the X-Request-Id variable'''
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as resp:
        header = resp.getheaders()
    wanted_key = "X-Request-Id"
    for key, value in header:
        if (key == wanted_key):
            print("{}".format(value))
