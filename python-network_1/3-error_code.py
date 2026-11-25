#!/usr/bin/python3
"""Display an HTTP error code or response using urllib."""

import sys
from urllib.error import HTTPError
from urllib.request import urlopen


if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print(f"Error code: {error.code}")
