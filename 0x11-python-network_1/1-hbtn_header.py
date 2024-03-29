#!/usr/bin/python3
"""Script that takes in URL, send request and diplays
value of X-Request-Id varible in header response.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
