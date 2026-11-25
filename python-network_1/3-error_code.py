#!/usr/bin/python3
"""Fetch a URL safely using the Python standard library.

Print the decoded response on success or the HTTP error status.
"""

import sys
from urllib.error import HTTPError
from urllib.request import urlopen


def main():
    """Run the HTTP response display from the command line."""
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print(f"Error code: {error.code}")


if __name__ == "__main__":
    main()
