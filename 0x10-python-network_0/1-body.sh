#!bin/bash
#Script that takes in a URL, sends a GET request to
#the URL, and displays the body of the response
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
