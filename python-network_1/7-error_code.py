#!/usr/bin/python3
"""Display the response text or numeric HTTP error code using requests."""

import sys

import requests


if __doc__ is None:
    __doc__ = "Report the response body or HTTP error code using requests."


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
