#!/usr/bin/python3

"""
Module: 4-hbtn_status
Fetches https://alx-intranet.hbtn.io/status using requests package.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))

