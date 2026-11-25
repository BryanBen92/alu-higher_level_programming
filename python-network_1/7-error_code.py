#!/usr/bin/python3
"""
Fetch a URL using requests and inspect its HTTP status.

Print the response text on success or the numeric HTTP error status.
"""

import sys

import requests


def main():
    """Run the HTTP response display from the command line."""
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
