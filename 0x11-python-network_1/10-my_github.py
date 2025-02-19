#!/usr/bin/python3
'''Python script that takes GitHub credentials'''
import requests
from sys import argv


if __name__ == "__main__":
    data = (argv[1], argv[2])
    resp = requests.get("https://api.github.com/user", data)
    if resp.status_code == 200:
        print(resp.json().get("id"))
    else:
        print("None")
