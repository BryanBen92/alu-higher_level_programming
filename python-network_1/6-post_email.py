#!/usr/bin/python3
"""Post an email field using requests and print the response."""

import sys

import requests


if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
