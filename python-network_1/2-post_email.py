#!/usr/bin/python3
"""Post an email field using urllib and print the response."""

import sys
from urllib.parse import urlencode
from urllib.request import urlopen


if __name__ == "__main__":
    data = urlencode({"email": sys.argv[2]}).encode("utf-8")
    with urlopen(sys.argv[1], data=data) as response:
        print(response.read().decode("utf-8"))
