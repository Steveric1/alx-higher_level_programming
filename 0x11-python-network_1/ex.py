#!/usr/bin/python3

import sys
import urllib.request

if __name__ == "__main__":
    get_url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(get_url) as res:
        if 'X-Request-Id' in res.headers:
            x_request_id = res.headers['X-Request-Id']
            print(x_request_id)