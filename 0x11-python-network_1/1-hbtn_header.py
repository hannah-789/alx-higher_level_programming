#!/usr/bin/python3

"""
Module: 1-hbtn_header
Fetches X-Request-Id variable value from the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)

