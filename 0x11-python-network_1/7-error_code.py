#!/usr/bin/python3
'''Script that takes in a URL, sends a request to the URL
 and displays the body of the response '''
import requests
from sys import argv
import urllib.error

if __name__ == "__main__":
    resp = requests.get(argv[1])
    if (resp.status.code >= 400):
        print("Error code: {}".format(resp.status.code))
    else:
        print(resp.text)
