#!/bin/bash
#Bash script that takes in a URL, sends a POST request to the passed URL
curl -s -X POST -d "email=$email&subject=$subject" $1
