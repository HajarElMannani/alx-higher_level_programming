#!/bin/bash
#Bash script that takes in a URL, sends a POST request to the passed URL
email="test@gmail.com"
subject="I will always be here for PLD"
curl -s -X POST -d "email=$email&subject=$subject" $1
