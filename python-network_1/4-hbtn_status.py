#!/usr/bin/python3
"""Fetch and display the ALU status response using requests."""

import requests


if __name__ == "__main__":
    body = requests.get("https://alu-intranet.hbtn.io/status").text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")
