#!/bin/bash
# Bash script to make a request to 0.0.0.0:5000/catch_me, triggering a response with the message "You got me!" in the body
curl -s -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me

