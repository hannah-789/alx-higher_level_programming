#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of a 200 status code response
curl -s -X GET "$1" -w "%{http_code}" -o /dev/null | grep -q 200 && curl -s "$1"

