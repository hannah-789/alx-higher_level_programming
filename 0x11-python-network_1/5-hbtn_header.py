#!/usr/bin/python3

"""
Module: 5-hbtn_header
Fetches the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])

