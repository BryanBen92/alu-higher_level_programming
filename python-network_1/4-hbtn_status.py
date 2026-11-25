#!/usr/bin/python3
"""Fetch the school status page with requests and display its text response."""

import requests


if __doc__ is None:
    __doc__ = "Fetch and display the school status page with requests."


if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    body = response.text
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
