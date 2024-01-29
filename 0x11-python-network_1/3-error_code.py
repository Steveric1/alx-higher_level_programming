#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
