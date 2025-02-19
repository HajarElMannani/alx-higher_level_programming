#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST
 request to http://0.0.0.0:5000/search_user with the letter
 as a parameter.'''
import requests
from sys import argv


if __name__ == "__main__":
    if (len(argv) == 1):
        q = ""
    else:
        q = argv[1]
    resp = requests.post('http://0.0.0.0:5000/search_user', {'q': q})
    if (resp.json()):
        print("[{}] {}".format(resp.json().get('id'),
                               resp.json().get('name')))
    else:
        print('No result')
