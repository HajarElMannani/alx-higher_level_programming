#!/bin/bash
#Script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -X GET -L $1
