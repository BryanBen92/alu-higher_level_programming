#!/usr/bin/python3
"""
Fetch a URL safely using the Python standard library.

Print the decoded response on success or the HTTP error status.
"""

import sys
import urllib.error
import urllib.request


def main():
    """Run the HTTP response display from the command line."""
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")


if __name__ == "__main__":
    main()
