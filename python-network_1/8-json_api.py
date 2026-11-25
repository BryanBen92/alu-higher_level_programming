#!/usr/bin/python3
"""Search the local API and display the resulting user."""

import sys

import requests


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data={"q": query})
    try:
        result = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if result:
            print("[{}] {}".format(result["id"], result["name"]))
        else:
            print("No result")
