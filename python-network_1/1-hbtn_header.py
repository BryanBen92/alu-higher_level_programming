#!/usr/bin/python3
"""Display the X-Request-Id response header using urllib."""

import sys
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
