#!/usr/bin/python3
"""
Fetch the school status endpoint using the requests library.

Display the type of the decoded response and its text.
"""

import requests


def main():
    """Run the HTTP response display from the command line."""
    body = requests.get("https://intranet.hbtn.io/status").text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")


if __name__ == "__main__":
    main()
