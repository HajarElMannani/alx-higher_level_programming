#!/bin/bash
#Bash script that takes in a URL as an argument sends a GET request to the URL
curl -s -X GET -H 'X-School-User-Id:98' $1
