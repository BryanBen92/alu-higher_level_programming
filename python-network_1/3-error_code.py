#!/usr/bin/python3
"""Display the UTF-8 response from a URL or report its HTTP error code."""

import sys
import urllib.error
import urllib.request


if __doc__ is None:
    __doc__ = "Report the response body or HTTP error code using urllib."


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code:", error.code)
