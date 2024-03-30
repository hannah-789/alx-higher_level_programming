#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, with the contents of a file as the body of the request, response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2" -L
