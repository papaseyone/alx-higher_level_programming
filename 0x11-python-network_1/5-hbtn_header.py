#!/usr/bin/python3
"""Displays the variable X-Request-Id in response header requested to URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
