#!/usr/bin/python3
"""
Fetch the school status endpoint using the Python standard library.

Display the raw response bytes, their type, and the decoded text.
"""

import urllib.request


def main():
    """Run the HTTP response display from the command line."""
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        body = response.read()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
    print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    main()
