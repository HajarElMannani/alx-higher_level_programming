#!/usr/bin/python3
'''Script that takes in a URL, sends a request to the URL
 and displays the body of the response '''
import urllib.request
from sys import argv
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as resp:
            body = resp.read().decode("utf-8")
        print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
