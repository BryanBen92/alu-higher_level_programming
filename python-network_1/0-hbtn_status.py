#!/usr/bin/python3
"""Fetch the school status page and display raw and decoded response data."""

import urllib.request


if __doc__ is None:
    __doc__ = "Fetch and display the school status page with urllib."


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
