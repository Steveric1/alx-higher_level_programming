#!/usr/bin/python3

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
